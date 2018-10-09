string = "   this is an important string   "

#remove white space from left side of string
string = string.lstrip()
print(string)

#remove white space from right side of string
string = string.rstrip()
print(string)

#remove all white space from string
string = string.strip()
print(string)

#capitalize first letter of string
string = string.capitalize()
print(string)

#change string to all UC
string = string.upper()
print(string)

#change string to all LC
string = string.lower()
print(string)

#how to create a list
list = ["a", "bunch", "of", "random", "words"]

#change a list into a string
string2 = " ".join(list)
print(string2)

#change a string into a list
string2 = string2.split()
print(string2)

#print each value in a list each time
for i in string2:
    print(i)

#count how many strings inside a string (Should count 2)
string = string.count("is")
print(string)

#find where string starts within a string (-1 will show if it cannot find)
string = "   this is an important string   "
string = string.find("this")
print(string)

#replace a substring with a substring
string = "   this is an important string   "
print(string.replace("an ", "a kind of "))

#creating an Acronym generator!!!

#Input String
x = str(input('Please enter a string: ')).split()
print(x)
#Return only first letter of every word
for y in x:
    print(y[0].capitalize(), end = '')

#change to upper case