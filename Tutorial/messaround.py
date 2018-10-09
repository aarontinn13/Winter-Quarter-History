import re

entry = 'singing in the shower'


if entry == 'singing in the shower':
    global pattern
    pattern = 'singing'
    print(pattern)
    if re.match(pattern, entry):
        print('yes')



pattern = r'spam'

'''To determine if the beginning matches'''
if re.match(pattern, 'spam'):
    print('match')
else:
    print('No Match')

