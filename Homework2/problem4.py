def max_of_three(a,b,c):
    if a > b:
        if a > c:
            print(a)
        else:
            print(c)
    else:
        if b > c:
            print(b)
        else:
            print(c)
try:
    a = raw_input('Please enter your first number: ')
    b = raw_input('Please enter your second number: ')
    c = raw_input('Please enter your third number: ')
    max_of_three(float(a),float(b),float(c))
#to check if values are numbers only
except ValueError:
    print('\nPlease type integer or decimal numbers only!\n')

#max function I think would iterate through a list like a map and and choose the highest as it reduces through.
