''' Real Python
Chapter 15.1 Let's get some practice with how to handle file dialogs by writing
a simple, usable program. We will guide the user (with GUI elements) through
the process of opening a PDF file, rotating its pages in some way, and then
saving the rotated file as a new PDF
'''

### Module(s) importation ###
from easygui import *
from PyPDF2 import PdfFileReader, PdfFileWriter

### Functions ###

### Parametrage ###

############
### MAIN ###
############

# let the user choose an input file
input_file_name = fileopenbox("", "Select a PDF to rotate...", "*.pdf")
if input_file_name is None:  #exit on "Cancel"
    exit()


# let the user choose an amount of rotation
rotate_choices = ('90', '180', '270')
message = "Rotate the PDF clockwise by how many degrees?"
degrees = int(buttonbox(message, 'Choose rotation' , rotate_choices))

# let the user choose an output file
output_file_name = filesavebox("", "Save the rotated PDF as...", "*.pdf")
while input_file_name == output_file_name: # cannot use same file as input
    msgbox("Cannot overwrite original file!", "Please choose another file...")
    output_file_name = filesavebox("", "Save the rotated PDF as...", "*.pdf")

if output_file_name is None:
    exit()  # exit on Cancel

# read in file, perform rotation and save out new file
input_file = PdfFileReader(open(input_file_name, "rb"))
output_PDF = PdfFileWriter()

for page_num in range(0, input_file.getNumPages()):
    page = input_file.getPage(page_num)
    page = page.rotateClockwise(int(degrees))
    output_PDF.addPage(page)

output_file = open(output_file_name, "wb")
output_PDF.write(output_file)
output_file.close() 





