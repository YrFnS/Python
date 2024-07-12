# Write a Python program to get system command output.

import os

print(os.popen('dir').read())
