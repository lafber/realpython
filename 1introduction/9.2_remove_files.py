''' Real Python
Assignment: Use pattern matching to delete files

Delete any JPG file found in any of these folders if the file is less than 2 Kb (2,000 bytes) in size in folder little pics

'''

import os

my_path = 'practice_files/little pics'

for current_folder, subfolders, file_names in os.walk(my_path):
    for file_name in file_names:
        my_file_path = os.path.join(my_path, file_name)
        if os.path.splitext(file_name)[1] == '.jpg' and os.path.getsize(my_file_path) < 2000: # bytes
            os.remove(my_file_path)
            print('File {} deleted'.format(my_file_path))