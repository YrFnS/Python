# Write a Python program to determine the profiling of Python programs.

import cProfile

test = 4 + 4 + 4 / 4 - 5 * 5
cProfile.run('print(test)')
