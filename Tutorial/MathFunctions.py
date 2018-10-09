import math

'''
can also import modules with an * so you don't have to type all the time
import math as *

can also import certain functions from modules using
from math import blah, bleh, blue

can rename a module's namespace using
import math as nigger

can see all of the functions inside of a module with 
dir(math)

to see all of the built in functions
import builtins
dir(builtins)

'''

print('ceil(4.4) = ', math.ceil(4.4)) #round up to 5
print('floor(4.4) = ', math.floor(4.4)) #round down to 4
print('fabs(4.4) = ', math.fabs(4.4)) #absolute value of 4.4

print('factorial(4) = ', math.factorial(4)) #factorial 4!
print('fmod(5,4) = ', math.fmod(4,5)) #modulo division
print('trunc(4.2) = ', math.trunc(4.2)) #receive a float and return only the integer, no rounding, whatever is left of the decimal
print('pow(2,2) = ', math.pow(2,2)) #2^2
print('sqrt(4) = ', math.sqrt(4)) #square root
print('math.e = ', math.e) #create e
print('math.pi = ', math.pi) #create pi
print('exp(4) = ', math.exp(4)) #return e^x
print('log(20) = ', math.log(20)) #return the natural log e * e * e ~= 20 so log(20) tells me that e^3 ~= 20
print('log(1000,10) = ', math.log(1000,10)) #you can define the base and 10^3 = 1000
print('log10(1000) = ', math.log10(1000)) #You can also use base 10 like this

#below are the following trig functions
# sin(x), cos, tan, asin, acos, atan, atan2, asinh, acosh,
# atanh, sinh, cosh, tanh

# convert radians to degrees and vice versa
print('degrees(1.5708) = ', math.degrees(1.5708))
print('radians(90) = ', math.radians(90))
