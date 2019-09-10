# https://realpython.com/working-with-files-in-python/

import os
from termcolor import colored

target = input("Which folder you want to invest?(default is posts)\n")

if target == "":
    target = "posts"

print("\n")
list_of_file_paths = []

for folder_name, sub_folders, filenames in os.walk(target):

    colored_folder_name = colored(folder_name, "yellow", attrs=["bold"])
    print(f"\tThe current folder is {colored_folder_name}")

    for subfolder in sub_folders:

        colored_subfolder = colored(subfolder, "yellow", attrs=["bold"])
        print(f"\tSUBFOLDER OF {folder_name}: {colored_subfolder}")

    for filename in filenames:

        colored_filename = colored(filename, "yellow", attrs=["bold"])
        print(f"\tFILE INSIDE {folder_name}: {colored_filename}")

        entire_file_path = f"{folder_name}/{filename}"
        colored_entire_file_path = colored(entire_file_path, "yellow", attrs=["bold"])
        print(f"\tThe entire path for the file: {colored_entire_file_path}\n")

        list_of_file_paths.append(entire_file_path)

print(f"\t{list_of_file_paths}\n")


