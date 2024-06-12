# Write a Python program to get OS name, platform and release information.

import os
import platform

print(f'Name: {os.name}')
print(f'Platform: {platform.system()}')
print(f'Release: {platform.release()}')
