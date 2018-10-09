import random
import math

numList = []

for i in range(5):
    numList.append(random.randrange(1,10))

numList.sort()   #sort in increasing order

numList.reverse()  #reverse the order of list

numList.insert(4, 10)  #insert at the 4th index, the number 10

numList.remove(10)  #remove the item "10" from the list

numList.pop(2)   #remove the item in index number 2

for i in numList:
    print(i)

#to print a list of even numbers, can use comprehension:
evenList = [i*2 for i in range(10)]

for i in evenList:
    print(i)

#multiple different calculations to perform within a list
numList = [1,2,3,4,5]
listofvalues = [[math.pow(m,2),math.pow(m,3),math.pow(m,4)] for m in numList]
for i in listofvalues:
    print(i)
print()

#multidimensional list
multiDlist = [[0] * 10 for i in range(10)]

multiDlist[0][1] = 10                   #first list, second position

print(multiDlist)

listTable = [[0] * 4 for i in range(4)]

for i in range(4):
    for j in range(4):
        listTable[i][j] = "{}:{}".format(i , j)

for i in range(4):
    for j in range(4):
        print(listTable[i][j], end="|")
    print()

