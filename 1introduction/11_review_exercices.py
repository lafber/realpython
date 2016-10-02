''' Real Python

Chapter 11 Review exercises

'''

### Module(s) importation ###
import os
from PyPDF2 import PdfFileReader, PdfFileWriter

### Functions ###

### Parametrage ###

path = 'practice_files'

############
### MAIN ###
############

input_file_name = os.path.join(path,'The Whistling Gypsy.pdf')
input_file = PdfFileReader(open(input_file_name, 'rb'))


# chapter 11 review ex 1 : 
print('-'*10, "Review exercice 1 chapter 11", '-'*10)
print("File: {} \nTitle: {} \nAuthor: {}\nTotal pages: {}\n".format(
    input_file_name, 
    input_file.getDocumentInfo().title,
    input_file.getDocumentInfo().author,
    input_file.getNumPages()))

# chapter 11 review ex 2 : Extract the full contents of The Whistling Gypsy.pdf into a .TXT file
print('-'*10, "Review exercice 2 chapter 11", '-'*10)

output_file_name = 'output/The Whistling Gypsy.txt'

with open(output_file_name, 'w') as output_file:
    for page in (0,input_file.getNumPages() - 1):
        output_file.writelines(input_file.getPage(page).extractText())
        
print("File {} created.".format(output_file_name))

# chapter 11 review ex 3
print('-'*10, "Review exercice 3 chapter 11", '-'*10)

output_pdf_name = 'output/The Whistling Gypsy No Cover.pdf'

with open(output_pdf_name, 'wb') as output_file:
    
    output_PDF = PdfFileWriter()
    
    for page in (1, input_file.getNumPages() - 1):
        output_PDF.addPage(input_file.getPage(page))

    output_PDF.write(output_file)

print("File {} created.".format(output_pdf_name))
