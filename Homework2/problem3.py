def password_test(password):
    #if length is greater than or equal to 12, we move on, else we fail first check.
    if len(password) >= 12:
        #if there are any digits we move on, else we fail second check
        if any(i.isdigit() for i in password):
            #if there are any characters we move on, else we fail third check
            if any(j.isalpha()for j in password):
                #if there are any of the special characters we move on, else we fail fourth check
                if ('!' in password) or ('@' in password)or('#' in password)or('$' in password)or('%' in password):
                    #if there are any upper case and lower case this is a strong password, else we fail fifth check
                    if any(x.isupper() for x in password) and any(x.islower() for x in password):
                        print('\nThis is a strong password\n')
                    else:
                        print('\nThis is not a strong password\n')
                else:
                    print('\nThis is not a strong password\n')
            else:
                print('\nThis is not a strong password\n')
        else:
            print('\nThis is not a strong password\n')
    else:
        print('\nThis is not a strong password\n')
#below is not an infinite loop since any 'break command' could be a password input
x = raw_input('''Enter a password with the following criteria to see if it is strong or not:
\n*Have at least 12 Characters
\n*Contains both numbers and letters
\n*Contains at least one of the following characters: !,@,#,$,%
\n*Contains at least one capital letter
\nPlease enter your password: ''')
password_test(str(x))
