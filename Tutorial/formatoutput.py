#make output in one line
for i in [1,2,3,4,5,6]:
    print(i,end=" ")            #end each iteration with...

print()
#make output separated by...
x = 5
y = 1
z = 4
print(x,y,z, sep = '.')

#string modulo operator
print(':%4d :%9f' % (float(123456789.123456789), float(123456789.123456789)))
'''
Example %6.2f is read as xxx.xx 
1.) Every modulo operator begins with a modulo symbol %
2.) The first number is the total number of places in the variable, in the above example, it is 6 total digits
3.) The decimal is optional if you want to round a certain number of decimals
4.) The number following the decimal is number how many digits you want to round to
5.) the last character can be defined by the following:
d	Signed integer decimal.
i	Signed integer decimal.
o	Unsigned octal.
u	Obsolete and equivalent to 'd', i.e. signed integer decimal.
x	Unsigned hexadecimal (lowercase).
X	Unsigned hexadecimal (uppercase).
e	Floating point exponential format (lowercase).
E	Floating point exponential format (uppercase).
f	Floating point decimal format.
F	Floating point decimal format.
g	Same as "e" if exponent is greater than -4 or less than precision, "f" otherwise.
G	Same as "E" if exponent is greater than -4 or less than precision, "F" otherwise.
c	Single character (accepts integer or single character string).
r	String (converts any python object using repr()).
s	String (converts any python object using str()).
%	No argument is converted, results in a "%" character in the result.

BELOW ARE A FEW EXAMPLES
'''
print('***********************************************************************************')
print("%10.3e"% (356.08977))
print("%10.3E"% (356.08977))
print("%10o"% (25))
print("%10.3o"% (25))
print("%10.5o"% (25))
print("%5x"% (47))
print("%5.4x"% (47))
print("%5.4X"% (47))
print("Only one percentage sign: %% " % ())

'''
#	Used with o, x or X specifiers the value is preceded with 0, 0o, 0O, 0x or 0X respectively.
0	The conversion result will be zero padded for numeric values.
-	The converted value is left adjusted
 	If no sign (minus sign e.g.) is going to be written, a blank space is inserted before the value.
+	A sign character ("+" or "-") will precede the conversion (overrides a "space" flag).
'''
print('***********************************************************************************')
print("%#5X"% (47))
print("%5X"% (47))
print("%#5.4X"% (47))
print("%#5o"% (25))
print("%+d"% (42))
print("% d"% (42))
print("%+2d"% (42))
print("% 2d"% (42))
print("%2d"% (42))



print('***********************************************************************************')

print("First argument: {0}, second one: {1}".format(47,11))
print("Second argument: {1}, first one: {0}".format(47,11))
print("Second argument: {1:3d}, first one: {0:7.2f}".format(47.42,11))
print("First argument: {}, second one: {}".format(47,11))
print("various precisions: {0:6.2f} or {0:6.3f}".format(1.4148))
print('{:5d}, Price: {:8.2f}'.format(453, 59.058))

print('***********************************************************************************')

print("{0:<20s} {1:6.2f}".format('Spam & Eggs:', 6.99))
print("{0:>20s} {1:6.2f}".format('Spam & Eggs:', 6.99))

'''
'<'	The field will be left-aligned within the available space. This is usually the default for strings.
'>'	The field will be right-aligned within the available space. This is the default for numbers.
'0'	If the width field is preceded by a zero ('0') character, sign-aware zero-padding for numeric types will be enabled.
            x = 378
            print("The value is {:06d}".format(x))
                The value is 000378
            x = -378
            print("The value is {:06d}".format(x))
                The value is -00378
','	This option signals the use of a comma for a thousands separator.
            print("The value is {:,}".format(x))
                The value is 78,962,324,245
            print("The value is {0:6,d}".format(x))
                The value is 5,897,653,423
            x = 5897653423.89676
            print("The value is {0:12,.3f}".format(x))
                The value is 5,897,653,423.897
'='	Forces the padding to be placed after the sign (if any) but before the digits. This is used for printing fields in the form "+000000120". This alignment option is only valid for numeric types.
'^'	Forces the field to be centered within the available space.

'+'	    indicates that a sign should be used for both positive as well as negative numbers.
'-'	    indicates that a sign should be used only for negative numbers, which is the default behavior.
space	indicates that a leading space should be used on positive numbers, and a minus sign on negative numbers
'''

print('************************************Dictionaries*****************************************')

print("The capital of {0:s} is {1:s}".format("Ontario","Toronto"))
print("The capital of {province} is {capital}".format(province="Ontario",capital="Toronto"))

data = dict(province="Ontario",capital="Toronto")
print("The capital of {province} is {capital}".format(**data))
#The double "*" in front of data turns data automatically into the form 'province="Ontario",capital="Toronto"'

capital_country = {"United States" : "Washington",
                   "US" : "Washington",
                   "Canada" : "Ottawa",
                   "Germany": "Berlin",
                   "France" : "Paris",
                   "England" : "London",
                   "UK" : "London",
                   "Switzerland" : "Bern",
                   "Austria" : "Vienna",
                   "Netherlands" : "Amsterdam"}

print("Countries and their capitals:")
for c in capital_country:
    print("{country}: {capital}".format(country=c, capital=capital_country[c]))

print()

capital_country = {"United States" : "Washington",
                   "US" : "Washington",
                   "Canada" : "Ottawa",
                   "Germany": "Berlin",
                   "France" : "Paris",
                   "England" : "London",
                   "UK" : "London",
                   "Switzerland" : "Bern",
                   "Austria" : "Vienna",
                   "Netherlands" : "Amsterdam"}

print("Countries and their capitals:")
for c in capital_country:
    format_string = c + ": {" + c + "}"
    print(format_string.format(**capital_country))

print()
print('*************************OTHER STRING METHODS***************************')

#there are four string methods, center(), ljust(), rjust(), zfill():

s = "Python"
print(s.center(10))
print(s.center(10,"*"))

print()

s = "Training"
print(s.ljust(12))
print(s.ljust(12,":"))

print()

s = "Programming"
print(s.rjust(15))
print(s.rjust(15, "~"))

print()

account_number = "43447879"
print(account_number.zfill(12))
#can be emulated such as below with rjust()
print(account_number.rjust(12,"0"))

print()

print('****************************STRING LITERALS**********************************')

price = 11.23
print(f"Price in Euro: {price}")

print(f"Price in Swiss Franks: {price * 1.086}")

print(f"Price in Swiss Franks: {price * 1.086:5.2f}")

for article in ["bread", "butter", "tea"]:
    print(f"{article:>10}:")

