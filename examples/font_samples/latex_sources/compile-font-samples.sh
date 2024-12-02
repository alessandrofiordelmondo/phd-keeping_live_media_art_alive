#! /bin/bash

# Default fonts
pdflatex Defaultfonts
biber    Defaultfonts
pdflatex Defaultfonts
pdflatex Defaultfonts

# Fira_Newtxsf
pdflatex Fira_Newtxsf
biber    Fira_Newtxsf
pdflatex Fira_Newtxsf
pdflatex Fira_Newtxsf

# Libertine
# pdflatex Libertine
# biber    Libertine
# pdflatex Libertine
# pdflatex Libertine

# Libertinus
pdflatex Libertinus
biber    Libertinus
pdflatex Libertinus
pdflatex Libertinus

# Lmodern
pdflatex Lmodern
biber    Lmodern
pdflatex Lmodern
pdflatex Lmodern

# Lucida
pdflatex Lucida
biber    Lucida
pdflatex Lucida
pdflatex Lucida

# Newtx-sans-text
pdflatex Newtx-sans-text
biber    Newtx-sans-text
pdflatex Newtx-sans-text
pdflatex Newtx-sans-text

# Newtx
pdflatex Newtx
biber    Newtx
pdflatex Newtx
pdflatex Newtx

# Heros-Stix2
lualatex Heros-Stix2
biber    Heros-Stix2
lualatex Heros-Stix2
lualatex Heros-Stix2

# Stix2
lualatex Stix2
biber    Stix2
lualatex Stix2
lualatex Stix2

# Termes-stix2
lualatex Termes-stix2
biber    Termes-stix2
lualatex Termes-stix2
lualatex Termes-stix2


# Termes
lualatex Termes
biber    Termes
lualatex Termes
lualatex Termes


# clean up

mkdir pdffiles
mv *.pdf pdffiles
rm *.aux
rm *.bbl
rm *.bcf
rm *.blg
rm *.log
rm *.lot
rm *.lof
rm *.toc
rm *.xml
