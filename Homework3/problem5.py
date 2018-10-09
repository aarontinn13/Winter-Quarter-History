def caesar_decrypt(key, message):
    #need a list to hold our decrypted message
    encrypted_message2 = []
    #for every letter in the message
    for i in message:
        #We are goin to retrieve the character code
        character_code = ord(i)
        #shift it down by the shift
        shift = character_code - key
        #if it is lower case
        if i.islower():
            #if it is less thn 97
            if shift < 97:
                #We need to bring it back by 26
                shift += 26
            #append this new letter to the list
            encrypted_message2.append(chr(shift))
        #if the letter is an upper case
        elif i.isupper():
            #if it is less than 65
            if shift < 65:
                #We will bring it back up by 26
                shift += 26
            #append the new letter to the list
            encrypted_message2.append(chr(shift))
        else:
            #anything that is not a character, we will add to the list
            encrypted_message2.append(i)
    #take the list and turn it into a string
    encrypted_message2 = ''.join(encrypted_message2)
    #return the new string
    return encrypted_message2

for i,j in enumerate(range(1,26)):
    print i,':',caesar_decrypt(i,'mpwtpgp jzf nly lyo jzf lcp slwqhlj espcp')


print('The key is: 11')
print('The message is: "believe you can and you are half way there"')
