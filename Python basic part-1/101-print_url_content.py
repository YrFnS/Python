# Write a Python program to access and print a URL's content to the console.

import urllib.request

link = 'https://www.google.com'

response = urllib.request.urlopen(link)

print(response.read())
