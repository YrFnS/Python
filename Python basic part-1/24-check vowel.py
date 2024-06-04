# Write a Python program to test whether a passed letter is a vowel or not

text = input('Enter a letter: ')

if text.lower() in ('a', 'e', 'i', 'o', 'u'):
    print('Vowel')
else:
    print('Not a vowel')
    