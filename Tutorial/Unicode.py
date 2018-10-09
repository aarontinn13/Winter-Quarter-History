#Computers store characters in computer called "Unicode"
#A-Z 65-90
#a-z 97-122

print("A = ", ord("A"))                     #gives us unicode for string(A)
print("65 = ", chr(65))                     #gives us the character for unicode "65"

#Input "Enter a string to hide in uppercase
String = str(input('Enter a string to hide in uppercase: '))
Code = ""
#Cycle through each character in the string
for i in String:
#Store each character code in a new string
    Code += str(ord(i) - 23)                #subtracting 23 to change lower case Unicode to 2 digits
#Print "Secret Message: "
print('Secret Message: ', Code)
#Cycle through each character code 2 at a time by incrementing by 2 each time
String = ""
for x in range(0, len(Code)-1, 2):
#Get the 1st and 2nd for the 2 digit number
    Char_Code = Code[x] + Code[x+1]
#Convert the code into characters and add thm to a new string
    String += chr(int(Char_Code) + 23)      #Adding 23 back to reverse above subtraction to print lower case
#Print "Original Message: "
print("Original Message : ", String)


