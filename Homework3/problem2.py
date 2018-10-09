def fahrenheit_to_celsius(i):
    #Takes your number and transforms to Celsius
    y = (i-32)*(5.0/9.0)
    #using format instead of % because decimal
    print '\nIt is {:0.2f} in Celsius...\n'.format(y)
#Below is an infinite loop, in order to escape, you must type 'break'
while True:
    try:
        x = raw_input('Enter a temperature in Fahrenheit \nor type \'break\' to escape: ')
        if x == 'break':
            print'\nBye\n'
            break
        else:
            fahrenheit_to_celsius(float(x))
    #exception handling for value errors
    except ValueError:
        print '\nPlease only enter integers or floats!\n'
