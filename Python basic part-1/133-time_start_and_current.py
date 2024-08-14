# Write a Python program to calculate the time runs (difference between start and current time) of a program.

import time

start = time.time()

time.sleep(1)

end = time.time()

difference = end - start

print('Time runs:', difference)

