''' Real Python
    Script Python générique pour exécuter les exemples du cours    
'''

import os
from PyPDF2 import PdfFileReader, PdfFileWriter

path = 'practice_files'

input_file_name = os.path.join(path,'Pride and Prejudice.pdf')
input_file = PdfFileReader(open(input_file_name,'rb'))
output_PDF = PdfFileWriter()

for page_num in range(1,4):
    output_PDF.addPage(input_file.getPage(page_num))
    
output_file_name = os.path.join(path, '../output/portion.pdf')
output_file = open(output_file_name, "wb")
output_PDF.write(output_file)
output_file.close()

