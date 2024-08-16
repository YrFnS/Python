# Write a Python program to find files and skip directories in a given directory.
import os

def find_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            print(os.path.join(root, file))

find_files("Python basic part-1")
