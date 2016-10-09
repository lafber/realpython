''' Real Python
Chapter 11.1 review exercice
'''

### Module(s) importation ###
import os 
import copy
from PyPDF2 import PdfFileReader, PdfFileWriter

### Functions ###

### Parametrage ###
path = 'practice_files'


############
### MAIN ###
############

# chapter 11.1 review ex 1 : Write a script that opens the file named Walrus.pdf
#   from the Chapter 11 practice files; you will need to decrypt the file using 
#   the password "IamtheWalrus"

input_file_name = os.path.join(path, 'Walrus.pdf')
input_file = PdfFileReader(open(input_file_name, 'rb'))
input_file.decrypt('IamtheWalrus') # decrypt password protected file

output_PDF = PdfFileWriter()

# chapter 11.1 review ex 2 : Rotate every page in this input file counter-clockwise by 90 degrees

for current_page in range(0, input_file.getNumPages()):
    page = input_file.getPage(current_page)
    page.rotateClockwise(-90) # rotate left 90°
    
    # chapter 11.1 review ex 3 : Split each page in half vertically, such that 
    # every column appears on its own separate page, and 
    page_left = input_file.getPage(current_page)
    page_right = copy.copy(page_left)
    
    upper_right = page_left.mediaBox.upperRight
    # changing coordinate of upper right of left page
    page_left.mediaBox.upperRight = (upper_right[0]/2, upper_right[1])
    output_PDF.addPage(page_left)
    
    # changing coordinate of upper left of right page
    page_right.mediaBox.upperLeft = (upper_right[0]/2, upper_right[1])
    output_PDF.addPage(page_right)
    
# output the results as a new PDF file in the Output folder
output_file_name = os.path.join(path, '../output/IAmTheCleanWalrus.pdf')
output_file = open(output_file_name, 'wb')
output_PDF.write(output_file)
output_file.close 

print("New pdf file {} generated".format(output_file_name))