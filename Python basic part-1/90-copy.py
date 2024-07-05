# Write a Python program to create a copy of its own source code.

def copy_file(src, dest):
    with open(__file__, 'r') as src:
        src = src.read()
    with open(dest, 'w') as dest:
        dest.write(src)

copy_file(__file__, 'copy_of_source_code.py')
