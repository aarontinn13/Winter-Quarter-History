#use 1 while loop and 3 for loops
#4 spaces : 1 hash
#3 spaces : 3 hashes
#2 spaces : 5 hashes
#1 space : 7 hashes
#0 spaces : 9 hashes

#Need to do
#Get number of rows for the tree
rows = eval(input('How tall is your tree: '))
#Decrement spaces by 1 each time through the loop
spaces = rows - 1
#Increment the hashes by 2 each time through the loop
hashes = 1
#Save spaces to the stump by calculating tree height - 1
stump_spaces = rows - 1
#Decrement from tree height until it equals 0
#Print spaces and then hashes for each row
#Print stump spaces and then 1 hash

while rows != 0:                     #while loop will finish before the for loop
    for i in range(spaces):
        print(' ',end='')
    for i in range(hashes):
        print('#', end='')
    print()                          #prints a new line
    spaces -= 1
    hashes += 2
    rows -= 1
for i in range(stump_spaces):
    print(' ', end='')

print('#')