# Write a Python program to validate an IP address.

from ipaddress import ip_address

def validate_ip(ip):
    try:
        ip_address(ip)
        print(True)
    except ValueError:
        print(False)

ip = input('Enter an IP address: ')
validate_ip(ip)
