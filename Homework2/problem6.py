def palindrome_tester(phrase):
    #takes raw phrase and removes all spaces
    phrase_without_spaces = phrase.replace(' ', '')
    #takes phrase and removes all special characters AND numbers
    phrase_alpha_numeric = ''.join(i for i in phrase_without_spaces if i.isalpha())
    #takes phrase and transforms all upper case to lower case
    phrase_all_lower_case = phrase_alpha_numeric.lower()
    #incase my string was only numbers and special characters, I have a check.
    if phrase_all_lower_case == '':
        print'This is not a palindrome.'
    #Final check to see if forward step is the same as reverse step.
    else:
        if phrase_all_lower_case == phrase_all_lower_case[::-1]:
            print'This is a palindrome.\n'
        else:
            print'This is not a palindrome.\n'

#no loop since any 'break command' could be an input 
string = raw_input('What is your word or phrase? ')
palindrome_tester(str(string))
