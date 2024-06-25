# Write a Python program to convert pressure in kilopascals to pounds per square inch, a millimeter of mercury (mmHg) and atmosphere pressure.

pressure = float(input('Enter pressure in kilopascals: '))

pounds = pressure / 6.89475729
mmHg = pressure * 760 / 101.325
atm = pressure / 101.325

print(f'Pounds per square inch: {pounds}\nMillimeter of mercury: {mmHg}\nAtmosphere pressure: {atm}')
