'''
Similar to functions except disposable and used when you need it
'''
def sum(x,y):
    return x + y
print(sum(3,4))

sum = lambda x, y : x + y
print(sum(3,4))

sum = (lambda x, y : x + y) (3,4)
print(sum)
print('**************************************************')


'''
MAP FUNCTION
takes an iterable through the lambda and returns a list of the iterables.
'''
C = [39.2, 36.5, 37.3, 38, 37.8]
F = list(map(lambda x: (float(9)/5)*x + 32, C))
print(F)

C = list(map(lambda x: (float(5)/9)*(x-32), F))
print(C)
print('**************************************************')

string_of_numbers = ['1','2','3']
int_of_numbers = [i for i in map( int,string_of_numbers)]
print(type(int_of_numbers[1]))
'''
map() can be applied to more than one list. The lists have to have the 
same length. map() will apply its lambda function to the elements of 
the argument lists, i.e. it first applies to the elements with the 0th 
index, then to the elements with the 1st index until the n-th index is reached: 
'''

a = [1,2,3,4]
b = [17,12,11,10]
c = [-1,-4,5,9]
print(list(map(lambda x,y:x+y, a,b)))
print(list(map(lambda x,y,z:x+y+z, a,b,c)))
print(list(map(lambda x,y,z : 2.5*x + 2*y - z, a,b,c)))
print('**************************************************')
'''
The map function of the previous chapter was used to apply one function 
to one or more iterables. We will now write a function which applies a 
bunch of functions, which may be an iterable such as a list or a tuple 
for example, to one Python object.
'''

from math import sin, cos, tan, pi

def map_functions(x, functions):
     """ map an iterable of functions on the the object x """
     res = []
     for func in functions:
         res.append(func(x))
     return res

family_of_functions = (sin, cos, tan)
print(map_functions(pi, family_of_functions))
print('**************************************************')
'''
FILTERING

offers an elegant way to filter out all the elements of a sequence 
"sequence", for which the function function returns True. i.e. an 
item will be produced by the iterator result of filter(function, sequence)
if item is included in the sequence "sequence" and if function(item) 
returns True.

In other words: The function filter(f,l) needs a function f as its first 
argument. f has to return a Boolean value, i.e. either True or False. 
This function will be applied to every element of the list l. Only if 
f returns True will the element be produced by the iterator, which is 
the return value of filter(function, sequence).

In the following example, we filter out first the odd and then the even 
elements of the sequence of the first 11 Fibonacci numbers:
'''

fibonacci = [0,1,1,2,3,5,8,13,21,34,55]
odd_numbers = list(filter(lambda x: x % 2 != 0, fibonacci))
print(odd_numbers)

even_numbers = list(filter(lambda x: x % 2 == 0, fibonacci))
print(even_numbers)

# or alternatively:

even_numbers = list(filter(lambda x: x % 2 -1, fibonacci))
print(even_numbers)


'''
REDUCE

The function 

reduce(func, seq) 

continually applies the function func() to the sequence seq. 
It returns a single value. 

If seq = [ s1, s2, s3, ... , sn ], calling reduce(func, seq) 
works like this:
At first the first two elements of seq will be applied to func, 
i.e. func(s1,s2) The list on which reduce() works looks now 
like this: [ func(s1, s2), s3, ... , sn ]

In the next step func will be applied on the previous result 
and the third element of the list, i.e. func(func(s1, s2),s3)

The list looks like this now: [ func(func(s1, s2),s3), ... , sn ]
Continue like this until just one element is left and return this 
element as the result of reduce()
'''
#adding
from functools import *
print(reduce(lambda x,y: x+y, [47,11,42,13])) #(((47+11)+42)+13)

#maximum from a list
f = lambda a,b: a if (a > b) else b
print(reduce(f, [47,11,42,102,13]))

print(reduce(lambda x, y: x+y, range(1,101)))
print(int((101)*(100/2)))

#orders problem
orders = [['34587', 'Learning Python, Mark Lutz',4,40.95],
        ['98762', 'Programming Python, Mark Lutz',5,56.80],
        ["77226", "Head First Python, Paul Barry", 3,32.95],
        ["88112", "Einfuhrung in Python3, Bernd Klein",3, 24.99]]

min_order = 100
print(list(map(lambda x : x if x[1] >= min_order else (x[0],x[1]+10),
           map(lambda x : (x[0],x[2]*x[3]),orders))))


