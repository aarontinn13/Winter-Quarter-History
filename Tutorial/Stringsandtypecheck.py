print(type(3))                                      #Print the type of information
print(type(3.14))
print(type("3"))
print(type('3'))
x = 123
print(id(x))                                        #get the id number of data

samp_string = "This is a very important string!"

print(samp_string[0])                               #Return the specific character in a string
print(samp_string[-1])
print(samp_string[3+5])

print("Length : ", len(samp_string))                #Return length of string
print(samp_string[0:4])                             #Return slice of string 0 - 4
print(samp_string[8:])                              #Return slice of string 8 - end
print(samp_string[::3])                             #Return slice of string beginning to end in increments of 3

print('green' + 'Eggs')                             #Concatenate

print('Hello ' * 5)                                 #multiply strings

num_string = str(4)                                 #Convert integer into a string
print(num_string)

for c in samp_string:                               #cycle through each character in a string (for loop each character)
    print(c)

for i in range(0, len(samp_string),2):              #range is 0 to 32, taking 2 characters at a time
    print(samp_string[i] + samp_string[i+1])        #print 2 at a time

