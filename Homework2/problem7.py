def pyramid(height):
    #will start the asterick count at one since there is only 1 at the top
    asterick_count = 1
    #keep space count the same as height so it is even at the end
    space_count = height
    #This while loop will repeat while decreasing to 0
    while height > 0:
        #each iteration will print spaces and astericks times their count
        print' '*space_count,'*'*asterick_count
        #each row increases asterick by 2
        asterick_count += 2
        #each row decreases space by 1
        space_count -= 1
        #to decrease the loop
        height -= 1

while True:
    try:
        x = raw_input('How tall is your Pyramid?\n or type \'break\' to leave ')
        if x == 'break':
            print'\nGoodbye!<333333\n'
            break
        pyramid(int(x))
    #To handle integer values only
    except ValueError:
        print'\nPlease only enter integer values.\n'
