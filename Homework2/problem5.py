def weird_algorithm(x):
    #turning the input into a list using list comprehension
    number_list = [int(j) for j in str(x)]
    #this should iterate through every other item in the list starting at the second index
    for i in number_list[1::2]:
        #multiplying by -2 to back out the number and keep the negative of it.
        i *= -2
        number_list.append(i)
    #will check if the number divided by 11 will produce a whole number.
    if sum(number_list)%11 == 0:
        print('\nThis is divisible by 11\n')
    else:
        print('\nThis is not divisible by 11\n')

try:
    x = raw_input('Please enter a number: ' )
    weird_algorithm(x)
except ValueError:
    print('\nPlease only enter an integer value\n')
