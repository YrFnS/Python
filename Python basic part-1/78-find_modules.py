# Write a Python program to find the available built-in modules.

import sys

module = sys.builtin_module_names

for name in module:
    print(name)
