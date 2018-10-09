# Problem: receive miles and convert to kilometers
# Kilometeres = miles * 1.60934
# Enter Miles 5
# 5 miles equals blah blah kilometers

Miles = input('Enter Miles: ')

Miles = int(Miles)                   #need to convert string to integer

Kilometers = Miles * 1.60934

print('{} miles = {} kilometers'.format(Miles, Kilometers))
