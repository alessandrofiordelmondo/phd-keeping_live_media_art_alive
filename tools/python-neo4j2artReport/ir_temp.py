def latex_fill(artist, artwork, year, description, conservation_statement, iteration_table):

    identity_report_latex=f"""
    \\documentclass[a4paper,12pt]{{article}}
    \\usepackage{{graphicx}} 
    \\usepackage[utf8]{{inputenc}}
    \\usepackage{{longtable}}
    \\usepackage{{booktabs}}

    \\begin{{document}}
    \\title{{Identity Report}}
    \\maketitle
    \\noindent
    \\begin{{minipage}}{{0.5\\textwidth}}
        \\large\\textbf{{Artist:}} {artist}\\newline
        \\large\\textbf{{Title:}}  {artwork}\\newline
        \\large\\textbf{{Year:}}  {year}\\newline
    \\end{{minipage}}
    \\hfill
    \\begin{{minipage}}{{0.48\\textwidth}} 
        \\centering
        \\includegraphics[width=\\textwidth]{{image.jpg}}
    \\end{{minipage}}

    \\section*{{Description}}
    {description}

    \\section*{{Conservation statement}}
    {conservation_statement}

    \\newpage
    \\section*{{Exhibition and Iteration History}}
    \\begin{{longtable}}{{|p{{0.1\\textwidth}}|p{{0.3\\textwidth}}|p{{0.5\\textwidth}}|}} 
    \\hline
    \\textbf{{N}} & \\textbf{{Date}} & \\textbf{{Venue - title}} \\\\ 
    \\hline
    \\endfirsthead
    {iteration_table}
    
    \\end{{longtable}}
    \\end{{document}}
    """

    output_file_name = f"{artwork}_identity_report.tex"

    with open(output_file_name, "w") as f:
        f.write(identity_report_latex)

    print("created latex file with name: "+output_file_name)
