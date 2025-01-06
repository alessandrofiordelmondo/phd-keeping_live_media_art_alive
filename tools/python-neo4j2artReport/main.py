from neo4j import GraphDatabase
import pandas as pd
import ir_temp as ir
import ts_temp as ts
import download_image as di

artworks_list = []

# Connect to Neo4j database
uri = "bolt://localhost:7687"  # Neo4j URI, change if needed
username = "neo4j"  # Your Neo4j username
password = "password"  # Your Neo4j password

# Initialize the driver
driver = GraphDatabase.driver(uri, auth=(username, password))

# Function to execute a query and return the results
def execute_query(query):
    with driver.session() as session:
        result = session.run(query)
        return result.data()  # returns data as a list of dictionaries


## GET LIST OF ARTWORKS IN THE DATABASE
def get_artworks_list():
    global artworks_list
    query =f"""
    MATCH (a:ARTWORK)
    RETURN a
    """
    artworks = execute_query(query)

    print(artworks)
    for n in range(len(artworks)):
        a = artworks[n]['a']['title']
        artworks_list.append(a)
        print(n, a)

## FOR IDENTITY REPORT
def get_artwork_info(a_title):
    a_query =f"""
    MATCH (a:ARTWORK {{title: '{a_title}'}})-[:ARTIST]->(p)
    RETURN a, p
    """
    i_query =f"""
    match (a:ARTWORK {{title: '{a_title}'}})-[:ITERATION_SERIE]->(i)
    return i
    """
    a = execute_query(a_query)
    i = execute_query(i_query)
    
    aa = a[0]['a']
    artist = ''+a[0]['p']['givenName']+' '+a[0]['p']['familyName']    
    
    ii = [] 
    for n in range(len(i)):
        i01 = i[n]['i']
        if len(i01['title']) > 0:
            # ii.append({'date': i01['date'], 'venue': ''+i01['title']+' - '+i01['venue']})
            ii.append({'date': i01['date'], 'venue': i01['venue']})
        else:
            ii.append({'date': i01['date'], 'venue': i01['venue']})
    
    return {'artwork': aa, 'artist': artist, 'iterations': ii}

def output_ir(a):
    aa = a["artwork"]
    artwork = aa["title"]
    year = aa["dateCreated"]
    description = aa["description"]
    conservation_statement = aa["conservationStatement"]
    
    di.download(aa["photo"], "image.jpg")

    artist = a["artist"]

    ii = a["iterations"]
    iteration_table =f""
    
    for n in range(len(ii)):
        iteration_table = iteration_table+"n"+" & "+str(ii[n]["date"])+" & "+ii[n]["venue"]+ "\\\\\\hline "

    ir.latex_fill(artist, artwork, year, description, conservation_statement, iteration_table)
    # print(aa)
    
## FOR TECHNICAL SHEET
def get_iteration_info(iteration, artwork):
    DATE = str(iteration[1])
    VENUE = iteration[0]
    iter_query =f"""
    match (i:ITERATION {{date:date('{DATE}'), venue: '{VENUE}'}})-[r]->(x)
    where type(r) IN ['BIT', 'DATA', 'PERFORMER']
    return x, labels(x) AS labels
    """

    sheet = {
        'people_list': [],
        'audio_equipment_list': [],
        'video_equipment_list': [],
        'generic_equipment_list': [],
        'computer_list': [],
        'musical_instrument_list': [],
        'audiovisual_list': [],
        'conceptual_mapping': [],
        'physical_implementation_mapping': [],
        'process_mapping': [],
        'temporal_mapping': [],
        'spatial_mapping': [],
        'graphical_mapping': [],
        'image_lists': []
    }
    i = execute_query(iter_query)

    PEOPLE = ''
    AUDIO_EQ_TABLE = ''
    VIDEO_EQ_TABLE = ''
    COMPUTER_TABLE = ''
    GENERIC_EQ_TABLE = ''
    M_INSTRUMENT_TABLE = ''
    VIDEO_TABLE = ''
    SPATIAL_MAPPING = ''
    CONCEPTUAL_MAPPING = ''
    PHYSICAL_MAPPING = ''
    PROCESS_MAPPING = ''
    TEMPORAL_MAPPING = ''
    GRAPHICAL_MAPPING = ''

    for n in range(len(i)):
        ii = i[n]['x']
        lab = i[n]['labels']
        if 'PERSON' in lab:
            PEOPLE = PEOPLE+ii['givenName']+' '+ii['familyName']+' '
        if 'AUDIO_EQUIPMENT' in lab:
            AUDIO_EQ_TABLE = AUDIO_EQ_TABLE+ii['format']+f"&"+ii['title']+f"\\\\\hline "
        elif 'VIDEO_EQUIPMENT' in lab:
            VIDEO_EQ_TABLE = VIDEO_EQ_TABLE+ii['format']+f"&"+ii['title']+f"\\\\\hline "
        elif 'COMPUTER' in lab:
            c_type = "computer hardware"
            if "SW_APPLICATION" in lab:
                c_type = "software app"
            elif "SW_ORIGINAL" in lab:
                c_type = "original software"
            elif "OS" in lab:
                c_type = "operating system"
            COMPUTER_TABLE = COMPUTER_TABLE+c_type+f"&"+ii['name']+f"\\\\\hline "
        elif 'GENERIC_EQUIPMENT' in lab:
            GENERIC_EQ_TABLE = GENERIC_EQ_TABLE+ii['format']+f"&"+ii['title']+f"\\\\\hline "
        elif 'M_INSTRUMENT' in lab:
            M_INSTRUMENT_TABLE = M_INSTRUMENT_TABLE+ii['title']+f"&"+''+f"\\\\\hline "
        elif 'VIDEO' in lab:
            VIDEO_TABLE = VIDEO_TABLE+ii['format']+f"&"+ii['title']+f"\\\\\hline "
        elif 'CONCEPTUAL_MAPPING' in lab:
            di.download(ii["identifier"], "conceptual_m.png")
            CONCEPTUAL_MAPPING = f"""
            \\subsection*{{Conceptual mapping}}
            {ii['description']}
            \\begin{{figure}}[h!]
            \\centering
            \\includegraphics[width=\\textwidth]{{conceptual_m.png}}
            \\end{{figure}}
            """
        elif 'PHYSICAL_IMPLEMENTATION_MAPPING' in lab:
            di.download(ii["identifier"], "physical_m.png")
            PHYSICAL_MAPPING = f"""
            \\subsection*{{Physical Implementation mapping}}
            {ii['description']}
            \\begin{{figure}}[h!]
            \\centering
            \\includegraphics[width=\\textwidth]{{physical_m.png}}
            \\end{{figure}}
            """
        elif 'PROCESS_MAPPING' in lab:
            di.download(ii["identifier"], "process_m.png")
            PROCESS_MAPPING = f"""
            \\subsection*{{Process mapping}}
            {ii['description']}
            \\begin{{figure}}[h!]
            \\centering
            \\includegraphics[width=\\textwidth]{{process_m.png}}
            \\end{{figure}}
            """
        elif 'SPATIAL_MAPPING' in lab:
            di.download(ii["identifier"], "spatial_m.png")
            SPATIAL_MAPPING = f"""
            \\subsection*{{Spatial mapping}}
            {ii['description']}
            \\begin{{figure}}[h!]
            \\centering
            \\includegraphics[width=\\textwidth]{{spatial_m.png}}
            \\end{{figure}}
            """
        elif 'GRAPHICAL_MAPPING' in lab:
            di.download(ii["identifier"], "graph_m.png")
            GRAPHICAL_MAPPING = f"""
            \\subsection*{{Graphical mapping}}
            {ii['description']}
            \\begin{{figure}}[h!]
            \\centering
            \\includegraphics[width=\\textwidth]{{graph_m.png}}
            \\end{{figure}}
            """
        elif 'TEMPORAL_MAPPING' in lab:
            di.download(ii["identifier"], "temporal_m.png")
            TEMPORAL_MAPPING = f"""
            \\subsection*{{Temporal mapping}}
            {ii['description']}
            \\begin{{figure}}[h!]
            \\centering
            \\includegraphics[width=\\textwidth]{{temporal_m.png}}
            \\end{{figure}}
            """

    ts.latex_fill(
        artwork['artist'], 
        artwork['artwork']['title'], 
        artwork['artwork']['dateCreated'], 
        DATE,
        VENUE,
        PEOPLE,
        AUDIO_EQ_TABLE,
        VIDEO_EQ_TABLE,
        COMPUTER_TABLE,
        GENERIC_EQ_TABLE,
        M_INSTRUMENT_TABLE,
        VIDEO_TABLE,
        SPATIAL_MAPPING,
        CONCEPTUAL_MAPPING,
        PHYSICAL_MAPPING,
        PROCESS_MAPPING,
        TEMPORAL_MAPPING,
        GRAPHICAL_MAPPING
    )

# iteration_info("Il tempo consuma")

# identity_report("Il tempo consuma")

if __name__ == "__main__":
    # print(age)
    get_artworks_list()
    artwork_title  = artworks_list[int(input("Artwork (enter the number) > "))]
    # try:
    artwork_info = get_artwork_info(artwork_title)
    print(f"\n Title: {artwork_info['artwork']['title']}\n Year: {artwork_info['artwork']['dateCreated']}\n Artist: {artwork_info['artist']}\n Number of iterations: {len(artwork_info['iterations'])}\n")
    mode  = int(input("Create 0) Identity Report 1) Technical Sheet. (Enter 0 or 1) > "))
    if mode < 1:
        output_ir(artwork_info)
    else:
        iterations_list = []
        for n in range(len(artwork_info['iterations'])):
            i = artwork_info['iterations'][n]
            iterations_list.append([i["venue"], i['date']])
            print(n, i['date'], i['venue'])
        
        get_iteration_info(iterations_list[int(input("Iteration (enter the number) > "))], artwork_info)
            
            
    # except:
    #     print("There is no artwork with that number.")