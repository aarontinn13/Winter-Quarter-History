import random
#This function is the game where we determine who is the winner or if there is a bad User input
def rock_paper_scissors(x):
    if x == 'rock':
        if computer_object == 'scissors':
            print '\nThe computer chose {}, you win!\n'.format(computer_object)
        else:
            print '\nThe computer chose paper, the computer wins :(\n'
    elif x == 'paper':
        if computer_object == 'rock':
            print '\nThe computer chose {}, you win!\n'.format(computer_object)
        else:
            print '\nThe computer chose scissors, the computer wins :(\n'
    elif x == 'scissors':
        if computer_object == 'paper':
            print '\nThe computer chose {}, you win!\n'.format(computer_object)
        else:
            print '\nThe computer chose rock, the computer wins :(\n'
    else:
        print '\nYou must choose paper, rock or scissors.\n'

def play_again():
    while True:
        y = raw_input('Would you like to play again? \n(Enter either \'y\' or \'n\') ')
        if y == 'y':
            return 'continue'
        elif y == 'n':
            return 'break'
        else:
            print '\nPlease only enter \'y\' to play again or \'n\' to quit!!!!!!\n'
            
#main while loop below
while True:
    #First determine both guesses
    x = raw_input('\nWhat is your guess? ')
    computer_object = random.choice(['paper', 'rock', 'scissors'])
    #second if the guesses are the same, restart.
    if x == computer_object:
        print('The computer chose {}, Let\'s settle this.'.format(computer_object))
        continue
    #Third we run the comparisons function and then run the play again function afterwards
    else:
        rock_paper_scissors(x)
        if play_again() == 'continue':
            continue
        else:
            print'\nGoodbye!<333333\n'
            break
