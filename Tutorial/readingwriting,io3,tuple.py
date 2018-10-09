#A tuple is like a list except it cannot be changed, created with (parenthesis)
myTuple = (1,2,3,4,5)

#how to print the first value
print('1st Value: ', myTuple[0])

#how to print the first 3 values
print(myTuple[0:3])

#how to print the length
print('Tuple Length: ', len(myTuple))

#how to concatenate tuples
moreFibs = myTuple + (13,21,34)

#how to check if an item is inside the tuple
print('32 in Tuple: ', 34 in moreFibs)

#how to print every item inside the tuple
for i in moreFibs:
    print(i)

#how to change a list to a tuple
aList = [55,89,144]
aTuple = tuple(aList)

#how to change a tuple to a list
aList = list(aTuple)

#how to get the max and min of tuples
print('Min: ', min(aTuple))
print('Max: ', max(aTuple))