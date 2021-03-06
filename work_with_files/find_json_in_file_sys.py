# the program finds files with desired extension and prints the path to them

import os


def find_obj(your_dir, your_file_format):
    searching_dir = os.walk(your_dir)
    for root, dirs, files in searching_dir:
        for file in files:
            if file.endswith(your_file_format):
                path_to_file = os.path.join(root, file)
                print(path_to_file)


directory = "C:\\Users\\User\\"
file_f = ".json"

find_obj(directory, file_f)


import glob


def search_by_glob(search_dir, file_type):
    os.chdir(search_dir)
    for file in glob.glob(f"{search_dir}**/*{file_type}", recursive=True):
        print(file)

search_by_glob(directory,file_f)
