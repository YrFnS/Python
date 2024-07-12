# Write a Python program to get the effective group id, effective user id, real group id, and a list of supplemental group ids associated with the current process.

import os

# Effective group ID
print(os.getegid())

# Effective user ID
print(os.geteuid())

# Real group ID
print(os.getgid())

# Supplemental group IDs
print(os.getgroups())
