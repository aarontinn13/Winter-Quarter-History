i = 1                       #i starts at 1

while i <= 20:              #while i is less than or equal to 20 we will run the below...
    if (i%2) == 0:          #if i is even we add 1 to i, if i is not even, we move down to next statement
        i += 1
        continue            #skip the bottom entirely and go back to the while statement

    if i == 15:             #stops the loop at 15
        break

    print("Odd : ", i)      #print statement and i

    i += 1                  #add 1 to i

