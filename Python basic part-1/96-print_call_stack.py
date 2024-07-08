# Write a Python program to print the current call stack.

import traceback

def file():
    text()

def text():
    for line in traceback.format_stack():
        print(line.strip())

file()
