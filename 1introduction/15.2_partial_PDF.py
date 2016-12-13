''' Real Python
Assignment: Use GUI elements to help a user modify files

Write a script partial_PDF.py that extracts a specific range of pages from a PDF file based
on file names and a page range supplied by the user. The program should run as follows

'''

### Module(s) importation ###
from easygui import *

from PyPDF2 import PdfFileReader, PdfFileWriter

### Functions ###

### Parametrage ###

############
### MAIN ###
############

# 1. Let the user choose a file using a fileopenbox
source_file_name = fileopenbox("Merci de choisir un fichier PDF à découper", "Fichier PDF source", "*.pdf")
if source_file_name is None:  # L'utlisateur a annulé
    exit()

input_pdf = PdfFileReader(open(source_file_name, 'rb'))
input_pdf_nb_pages = input_pdf.getNumPages()


# 2. Let the user choose a begining page to select using an enterbox
page_begin = enterbox("A quelle page (incluse) souhaitez-vous débuter la découpe", "Choix page début découpe")

# 3. If the user enters invalid input
# la page de début est-elle valide ?
#  - un entier positif
#  - un numéro de page inférieur ou égal au nombre total de pages du pdf
while (    not page_begin.isdigit()
        or int(page_begin) > input_pdf_nb_pages):
    msgbox("Merci de saisir un entier positif inférieur au nombre total de pages")
    page_begin = enterbox("A quelle page (incluse) souhaitez-vous débuter la découpe", "Choix page début découpe")
    if page_begin is None:
        exit()

# 4. Let the user choose an ending page using another enterbox
page_end = enterbox("A quelle page (incluse) souhaitez-vous finir la découpe", "Choix page fin découpe")

# 5. If the user enters an invalid ending page, use a msgbox to let the user know that
# was a problem, then ask for a beginning page again using an enterbox
while (    not page_end.isdigit()
        or int(page_end) > input_pdf_nb_pages
        or int(page_end) < int(page_begin)):
    msgbox("Merci de saisir un entier positif inférieur au nombre total de pages")
    page_end = enterbox("A quelle page (incluse) souhaitez-vous finir la découpe", "Choix page fin découpe")
    if page_end is None:
        exit()
        
# 6. Let the user choose an output file name using a savefilebo
output_file_name = filesavebox("", "Sauvegarder le pdf découpé en ...", "*.pdf")
if output_file_name is None:
    exit()


# 7. If the user chooses the same file as the input file, let the user know the problem using a msgbox
# then ask again for a file name using a savefilebox
while output_file_name == source_file_name:
    msgbox("Votre fichier découpé ne peut pas être identique au pdf source", "Merci de choisir un autre fichier")
    output_file_name = filesavebox("", "Sauvegarder le pdf découpé en ...", "*.pdf")
    if output_file_name is None:
        exit()


#8. Output the new file as a section of the input file based on the user- supplied page range.
# The user should be able to supply "1" to mean the first page of the document. 
output_PDF = PdfFileWriter()
# subtract 1 from supplied start page number to get correct index value
for page_num in range(int(page_begin) - 1, int(page_end)):
    page = input_pdf.getPage(page_num)
    output_PDF.addPage(page)
output_file = open(output_file_name, "wb")
output_PDF.write(output_file)
output_file.close()

