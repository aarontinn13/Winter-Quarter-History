#Guess a number between 1 and 10:
#if you get it wrong it will ask again until you get it right
import random
secret_number = random.randrange(1,11)


while True:
    try:
        random_number = eval(input('Guess a number between 1 and 10: '))
        if random_number == secret_number:
            print('You guessed correctly')
            break
        else:
            print('Please try again')
    except:
        print('Please enter a number from 1 through 10')




