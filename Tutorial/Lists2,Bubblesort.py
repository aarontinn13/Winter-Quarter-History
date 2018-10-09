'''
Bubble Sort:
1. An outer loop decreases in size each time
2. The goal is to have the largest number at the end of
   the list when the outer loop completes 1 cycle
3. The inner loop starts comparing indexes at the
   beginning of the loop
4. Check if list[index] > list[index + 1]
5. If so swap the index values
6. When the inner loop completes the largest number
   is at the end of the list
7. Decrement the outer loop
'''

import random

numList = [19, 1, 9, 7, 3, 10, 13, 15, 8, 12]

#for i in range(5):
    #numList.append(random.randrange(1,10))

i = len(numList) - 1 #The reason behind subtracting 1 is because the list starts at 0 index and would give out of bounds

print(numList)

while i > 1:
    j = 0
    while j < i:

        print("\nIs {} > {}".format(numList[j], numList[j+1]))

        if( numList[j] > numList[j + 1]):
            print('Switch')

            temp = numList[j]
            numList[j] = numList[j + 1]
            numList[j + 1] = temp
        else:
            print("Don't Switch")

        j += 1

        for k in numList:
            print k ,
        print
    print('END OF ROUND')

    i -= 1

for k in numList:
    print k,

print