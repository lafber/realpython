''' Real Python
    Assignment: Split a CSV file


    
'''

### Module(s) importation ###
import argparse  # https://docs.python.org/3.5/library/argparse.html
import os 
import csv

### Parametrage ###
output_path = ''
csv_header = 'y'
csv_delimiter = ','

### Functions 

## output file name generator
def set_output_file_name( file_name, current_chunk):
    # insert the current chunk number in the  output file asked
    return os.path.splitext(file_name)[0] + '_' + str(current_chunk) + os.path.splitext(file_name)[1]


### MAIN ###

#CLI parser definition 
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input_file", help="input file name")
parser.add_argument("-o", "--output_file", help="output file name")
parser.add_argument("-r", "--row_limit", help="row limit to split", type=int)
args = parser.parse_args()


# Input file exist ? 
if os.path.isfile(args.input_file) == False: 
    print("Error : {} is not a valid file".format(args.input_file))

# reading input file
with open(args.input_file, 'r') as source_file:
    
    all_lines = source_file.readlines()
    
    # input file has more line than the row split ask ? 
    source_lines_nb = len(all_lines)
    if source_lines_nb < args.row_limit:
        print("Error : {} has less than {} lines".format(args.input_file, args.row_limit))
    else:
        print("Begin splitting file {} in {} lines files".format(args.input_file, args.row_limit))

    current_row = 0 #counter for line
    current_chunk = 1 
    output_list = {}
    output_list[1] = []

#   Reading each line of the source file      
    for line in all_lines:
        output_list[current_chunk].append(line)
        current_row += 1

        # At the row limit ? 
        if current_row == args.row_limit:
            current_chunk += 1   # new chunk
            current_row = 0      # reset line counter
            output_list[current_chunk] = [] #create a new list for the new chunk

        
#   writing to output file n°<chunk>
    for chunk in output_list:
        with open(set_output_file_name(args.output_file, chunk),'w') as chunk_output_file:
            chunk_output_file.writelines(output_list[chunk])
        print("File {} created with {} lines.".format(set_output_file_name(args.output_file, chunk), len(output_list[chunk])))


# the command line I used with the INSEE file of the gold indice value each month. 320 lines.
# python3 9.5_split_csv.py -i practice_files/cours-or-insee.csv -o output/cours-or.csv -r 100 
