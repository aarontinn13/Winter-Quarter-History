letter_z = "z"
num_3 = "3"
a_space = ' '
float_pi = "3.14"

print('is z a letter or number: ', letter_z.isalnum()) #check if string is letter or numbers

print('is z a letter: ', letter_z.isalpha()) #check if string is letters only

print('is 3 a number: ', num_3.isdigit()) #check if string is numbers only

print('is z lowercase: ', letter_z.islower()) #check if string is all lowercase

print('is z uppercase: ', letter_z.isupper()) #check if string is all uppercase

print('is space a space: ', a_space.isspace()) #check if string is a whitespace

#encrypt a message

message = input("Enter your message: ")
key = int(input("How many characters should we shift (1-26): "))

secret_message = ''

for char in message:
    if char.isalpha():
        char_code = ord(char)
        char_code += key

        if char.isupper():
            if char_code > ord('Z'):
                char_code -= 26
            if char_code < ord('A'):
                char_code += 26
        else:
            if char_code > ord('z'):
                char_code -= 26
            if char_code < ord('a'):
                char_code += 26

        secret_message += chr(char_code)

    else:
        secret_message += char

print("Encrypted: ", secret_message)

#decrypt

key = -key
orig_message = ""

for char in secret_message:
    if char.isalpha():
        char_code = ord(char)
        char_code += key

        if char.isupper():
            if char_code > ord('Z'):
                char_code -= 26
            if char_code < ord('A'):
                char_code += 26
        else:
            if char_code > ord('z'):
                char_code -= 26
            if char_code < ord('a'):
                char_code += 26

        orig_message += chr(char_code)

    else:
        orig_message += char

print("Decrypted: ", orig_message)

