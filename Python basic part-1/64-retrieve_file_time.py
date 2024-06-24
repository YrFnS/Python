# Write a Python program that retrieves the date and time of file creation and modification.

import os.path, time

print('Created at ', time.ctime(os.path.getctime('Python basic part-1')))
print('Modified at ',time.ctime(os.path.getmtime('Python basic part-1')))
