''' Real Python
    Review exercices 9.1

    
'''

import os
import glob

my_path = './practice_files/images'

# 1 Display the full paths of all of the files and folders in the images folder by using os.listdir()
print('1', '-'*20)

for file_name in os.listdir(my_path):
    print(os.path.join(my_path, file_name))


# 2 Display the full paths of any PNG files in the images folder by using glob.glob()
print('2', '-'*20)

for file_name in glob.glob(os.path.join(my_path, '*.png')):
    print(file_name,)

# 3 Rename any PNG files in the images folder and its subfolders to be JPG files by using os.walk() 
print('3', '-'*20)

for current_folder, subfolders, file_names in os.walk(my_path):
    for file_name in file_names:
        file_tuple = os.path.splitext(file_name)
        if file_tuple[1] == '.png':
            print('this file extension {} should be changed'.format(os.path.join(current_folder,file_name)))
        # not doing the renaming 

# 4 Make sure that your last script worked by using os.path.exists() to check that the
# JPG files now exist (by providing os.path.exists() with the full path to each of these files)
print('4', '-'*20)

print(os.path.exists(os.path.join(my_path, "png file - not a gif.jpg")))
print(os.path.exists(os.path.join(my_path, "additional files/one last image.jpg")))