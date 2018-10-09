import random
import math

maximum = int(input('What is the Max? '))

#create the multidimensional list
multTable = [[0] * maximum for i in range(maximum)]
#increment with outer for
for i in range(1,maximum):
    #increment with inner for
        for j in range(1,maximum):
        #Assign the value to the cell
            multTable[i][j] = i * j
#Output the data
for i in range(1,maximum):
    for j in range(1,maximum):
        print(multTable[i][j], end=", ")
    print()
