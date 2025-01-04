from neo4j import GraphDatabase
import pandas as pd
import ir_temp as ir
import download_image as di

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

def iteration_info(a_title):
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
            ii.append({'date': i01['date'], 'venue': ''+i01['title']+' - '+i01['venue']})
        else:
            ii.append({'date': i01['date'], 'venue': i01['venue']})
    
    return {'artwork': aa, 'artist': artist, 'iterations': ii}

def identity_report(artwork_title):
    a = iteration_info(artwork_title)
    aa = a["artwork"]
    artwork = aa["title"]
    year = aa["dateCreated"]
    description = aa["description"]
    conservation_statement = aa["conservationStatement"]
    
    di.download(aa["photo"])

    artist = a["artist"]

    ii = a["iterations"]
    iteration_table =f""
    
    for n in range(len(ii)):
        iteration_table = iteration_table+"n"+" & "+str(ii[n]["date"])+" & "+ii[n]["venue"]+ "\\\\\\hline "

    ir.latex_fill(artist, artwork, year, description, conservation_statement, iteration_table)
    # print(aa)
    

identity_report("Il tempo consuma")