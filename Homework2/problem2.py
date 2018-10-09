def score(x):
    if 90 <= x <=100:
        print '\nYou received an A!\n'
    elif 80 <= x <90:
        print '\nYou received an B!\n'
    elif 70 <= x <80:
        print '\nYou received an C!\n'
    elif 60 <= x <70:
        print '\nYou received an D!\n'
    elif 0 <= x < 60:
        print '\nYou received an F!\n'
    else:
        #This else conditional should take care of any integers that fall outside of 1-100
        print '\nPlease enter an integer from 1 to 100\n'
while True:
    #This will
    x = raw_input('Enter a score \nor type \'break\' to escape: ')
    if x == 'break':
        print'\nGoodbye!<333333\n'
        break
    try:
        score(int(x))
    #exception handling for value errors
    except ValueError:
        print '\nPlease enter an integer from 1 to 100\n'
