text = input('')

if text.startswith('Is'):
    print('\n' + text)
elif text.startswith('is'):
    print('\n' + text)
else:
    print(f'\nIs {text}')
