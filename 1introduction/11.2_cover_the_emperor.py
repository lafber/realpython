''' Real Python
chapitre 11.2 Assignment: Add a cover sheet to a PDF file
'''

### Module(s) importation ###
import os
from PyPDF2 import PdfFileReader, PdfFileWriter


### Functions ###

### Parametrage ###
source_path = 'practice_files'
target_path = 'output'

############
### MAIN ###
############


# opening source PDF
source_pdf = PdfFileReader(open(os.path.join(source_path, 'The Emperor.pdf'), 'rb'))

# opening cover sheet PDF
cover_pdf = PdfFileReader(open(os.path.join(source_path, 'Emperor cover sheet.pdf'), 'rb'))

target_pdf = PdfFileWriter()

# append cover page to target pdf
target_pdf.appendPagesFromReader(cover_pdf)
# append source pdf to target pdf
target_pdf.appendPagesFromReader(source_pdf)


# saving target pdf
target_file = open(os.path.join(target_path, 'The Covered Emperor.pdf'), 'wb')
target_pdf.write(target_file)
target_file.close 

print('New covered pdf created')