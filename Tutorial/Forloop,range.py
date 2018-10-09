'''
for <variable> in <sequence>:
	<statements>
else:
	<statements>
'''

#loop through all numbers in the brackets
for i in [2,4,6,8,10]:
    print('i = ', i)
#loop through all the numbers starting from 0 going up all the way to 9
for n in range(10):
    print('n = ', n)
#loop through all the numbers starting at 2 going up to 9
for x in range(2,10):
    print('x = ', x)
#using modulo to find if a number is even or odd
a = 2
print((a % 2) == 0) #output should be True to indicate a is even

#print the odd numbers from 1-20
for b in range(1, 21):
    if (b%2) != 0:
        print('b = ', b)

