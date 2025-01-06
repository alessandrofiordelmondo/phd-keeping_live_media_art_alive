def latex_fill(artist, artwork , year, date, venue, 
               people, 
               audio_eq_table, video_eq_table, computer_table, generic_eq_table, m_instrument_table, video_table,
               spatial_mapping, conceptual_mapping, physical_mapping, process_mapping, temporal_mapping, graphical_mapping
               ):

    identity_report_latex=f"""
    \\documentclass[a4paper,12pt]{{article}}
    \\usepackage{{graphicx}} 
    \\usepackage[utf8]{{inputenc}}
    \\usepackage{{longtable}}
    \\usepackage{{booktabs}}

    \\begin{{document}}
    \\title{{Technical Sheet}}
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
    \\newline
    \\textbf{{Technical Sheet}} from {venue} - {date} \\newline
    \\section*{{People}}
    {people}
    \\section*{{Components lists}}
    
    % Audio Equipment
    \\begin{{longtable}}{{|p{{0.45\\textwidth}}|p{{0.45\\textwidth}}|}} 
    \\caption{{Audio Equipment}} \\\\\hline
    \\textbf{{Type}} & \\textbf{{Name}}\\\\ 
    \\hline
    \\endfirsthead
    {audio_eq_table}
    \\end{{longtable}}
    
    % Video Equipment
    \\begin{{longtable}}{{|p{{0.45\\textwidth}}|p{{0.45\\textwidth}}|}} 
    \\caption{{Video Equipment}} \\\\\hline
    \\textbf{{Type}} & \\textbf{{Name}}\\\\ 
    \\hline
    \\endfirsthead
    {video_eq_table}
    \\end{{longtable}}
    
    % Computer
    \\begin{{longtable}}{{|p{{0.45\\textwidth}}|p{{0.45\\textwidth}}|}} 
    \\caption{{Computer and software}} \\\\\hline
    \\textbf{{Type}} & \\textbf{{Name}}\\\\ 
    \\hline
    \\endfirsthead
    {computer_table}
    \\end{{longtable}}
    
    % Generic Equipment
    \\begin{{longtable}}{{|p{{0.45\\textwidth}}|p{{0.45\\textwidth}}|}} 
    \\caption{{Generic Equipment}} \\\\\hline
    \\textbf{{Type}} & \\textbf{{Name}}\\\\ 
    \\hline
    \\endfirsthead
    {generic_eq_table}
    \\end{{longtable}}
    
    % Musical Instrument
    \\begin{{longtable}}{{|p{{0.45\\textwidth}}|p{{0.45\\textwidth}}|}} 
    \\caption{{Musical Instruments}} \\\\\hline
    \\textbf{{Type}} & \\textbf{{Name}}\\\\ 
    \\hline
    \\endfirsthead
    {m_instrument_table}
    \\end{{longtable}}
    
    % Video 
    \\begin{{longtable}}{{|p{{0.45\\textwidth}}|p{{0.45\\textwidth}}|}} 
    \\caption{{Audiovisuals}} \\\\\hline
    \\textbf{{Type}} & \\textbf{{Name}}\\\\ 
    \\hline
    \\endfirsthead
    {video_table}
    \\end{{longtable}}

    \\section*{{Mappings}}
    {spatial_mapping}
    {conceptual_mapping}
    {physical_mapping}
    {process_mapping}
    {temporal_mapping}
    {graphical_mapping}
    \\end{{document}}
    """

    with open("technical_sheet.tex", "w") as f:
        f.write(identity_report_latex)
