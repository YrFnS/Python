# Write a Python program to check whether a file path is a file or a directory.

import os

def check_path(path):
    if os.path.isfile(path):
        print(f"{path} is a file.")
    elif os.path.isdir(path):
        print(f"{path} is a directory.")
    else:
        print(f"{path} is neither a file nor a directory.")

check_path('Python basic part-1')
check_path('Python basic part-1/85-checK_file.py')
check_path('Python basic part-1/85-checK_file.py.txt')
