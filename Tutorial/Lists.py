import random
import math

'''
below is an example of a list, the left is the index number and the right is the data which can be strings to variables

[0 : "string"] [1 : 1.234] [2 : 28] [3 : "c"]
'''
#below is an example of list named "randList"
randList = ['string', 1.234, 28]

'''
#below are two ways to turn a variable into a list
randList = []
randList = list(randList)
'''

#you can use the range function to make a list from 1 - 10
onetoTen = list(range(10))

#append a list within another list
randList.append(onetoTen)
print(1,randList)

#remove an item from a list
randList.remove(1.234)
print(2,randList)

#instead of append, we can extend a list with information from another list using the type from the first list

randList.extend(onetoTen)
print(3,randList)
#OR create a new variable
X = randList + onetoTen
print(4,X)


#can concatenate lists like below
randList = randList + onetoTen

#can print the data from the index number, for example if we wanted the first data. result should print out string
print(5,randList[0])

#can get the length of a list
print(6,'The length of the list is: ', len(randList))

#can get the "slice" or a subset of infomation from the list
first3 = randList[0:3]

#can retrieve the index number and data through a for loop
for i in first3:
    print(7,'{} : {}'.format(first3.index(i), i))

#can get data multiple times
print(8,(first3[0]) * 3)

#can see if data is or is not in a list
print(9,'string' in first3)
print(10,'noh' not in first3)

#can see what index the data is in
print(11,'Index of String: ', first3.index('string'))

#count how many times a certain data appears in the list
print(12,'How many strings: ', first3.count("string"))

#can change a data in a certain index position
first3[0] = 'new string'
for i in first3:
    print(13,'{} : {}'.format(first3.index(i), i))

#can add data to a list
first3.append('Another')
for i in first3:
    print(14,'{} : {}'.format(first3.index(i), i))

#generate a list of 5 random numbers 1 - 9

for i in range(5):
    print(15,random.randrange(1,10))

#OR

numList = []

for i in range(5):
    numList.append(random.randrange(1,10))

for i in numList:
    print(i)

