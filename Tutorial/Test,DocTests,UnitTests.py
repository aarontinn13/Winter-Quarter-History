'''
This paragraph is about unit tests. As the name implies they are
used for testing units or components of the code, typically, classes
or functions. The underlying concept is to simplify the testing of
large programming systems by testing "small" units. To accomplish
this the parts of a program have to be isolated into independent
testable "units". One can define "unit testing" as a method whereby
individual units of source code are tested to determine if they
meet the requirements, i.e. return the expected output for all
possible - or defined - input data. A unit can be seen as the
smallest testable part of a program, which are often functions or
methods from classes. Testing one unit should be independent from
the other units. As a unit is "quite" small, i.e. manageable to
ensure complete correctness. Usually, this is not possible for
large scale systems like large software programs or operating systems.
'''

""" Fibonacci Module """

'''
Every module has a name, which is defined in the built-in attribute
__name__. Let's assume that we have written a module "xyz" which we 
have saved as "xyz.py". If we import this module with "import xyz", 
the string "xyz" will be assigned to __name__. If we call the file 
xyz.py as a standalone program, i.e. in the following way, 

$python3 xyz.py
'''
def fib(n):
    """ Calculates the n-th Fibonacci number iteratively """
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

def fiblist(n):
    """ creates a list of Fibonacci numbers up to the n-th generation """
    fib = [0,1]
    for i in range(1,n):
        fib += [fib[-1]+fib[-2]]
    return fib

if fib(0) == 0 and fib(10) == 55 and fib(50) == 12586269025:
    print("Test for the fib function was successful!")
else:
    print("The fib function is returning wrong values!")

'''
doctest Module

The doctest module is often considered easier to use than the unittest, 
though the later is more suitable for more complex tests. doctest is a 
test framework that comes prepackaged with Python. The doctest module 
searches for pieces of text that look like interactive Python sessions 
inside of the documentation parts of a module, and then executes 
(or reexecutes) the commands of those sessions to verify that they work 
exactly as shown, i.e. that the same results can be achieved. In other 
words: The help text of the module is parsed for example python sessions. 
These examples are run and the results are compared against the expected value.

Usage of doctest:
To use "doctest" it has to be imported. The part of an interactive Python 
sessions with the examples and the output has to be copied inside of the 
docstring the corresponding function.

We demonstrate this way of proceeding with the following simple example. 
We have slimmed down the previous module, so that only the function fib is left:
'''

import doctest

def fib(n):
    """ Calculates the n-th Fibonacci number iteratively """
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

