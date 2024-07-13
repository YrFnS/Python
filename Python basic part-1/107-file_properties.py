# Write a Python program to retrieve file properties.

import os
import time

file = __file__

# Access time  
print(time.ctime(os.path.getatime(file)))

# Modified time
print(time.ctime(os.path.getmtime(file)))

# Change time
print(time.ctime(os.path.getctime(file)))

# Size
print(os.path.getsize(file))
