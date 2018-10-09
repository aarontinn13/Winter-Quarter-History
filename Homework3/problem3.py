def caesar_encrypt(key, message):
    #need a list to hold our encrypted message
    encrypted_message = []
    #for every letter in the message...
    for i in message:
        #we are going to retrieve the character code
        character_code = ord(i)
        #and shift it up by the key
        shift = character_code + key
        #if character is a lower case letter
        if i.islower():
            #if the code is above 122
            if shift > 122:
                #we need to bring the shift down by 26
                shift -= 26
            #then append this new letter to the list
            encrypted_message.append(chr(shift))
        #If the character is an upper case letter
        elif i.isupper():
            #If the shift is above 90
            if shift > 90:
                #we bring it back down by 26
                shift -= 26
            #append this new letter to the list
            encrypted_message.append(chr(shift))
        else:
            #anything that is not a character, we will add to the list
            encrypted_message.append(i)
    #take the list and turn it into a string
    encrypted_message = ''.join(encrypted_message)
    #return the new string
    return encrypted_message

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


key = 5
message = 'Hello World'
messed_up_message = caesar_encrypt(key, message)

print(messed_up_message)
print(caesar_decrypt(key, messed_up_message))
