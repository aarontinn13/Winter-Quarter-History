'''
A decorator in Python is any callable Python object that is used to modify a function or a class.
A reference to a function "func" or a class "C" is passed to a decorator and the decorator returns
a modified function or class. The modified functions or classes usually contain calls to the original
function "func" or class "C".
'''

def succ(x):
    return x + 1

successor = succ                   #creating variable successor; which also calls succ
print(successor(10))               #calling successor function
print(succ(10))                    #calling succ function

print()
print('*********************************************************************************************')
print()


''' FUNCTIONS WITHIN FUNCTIONS'''
def temperature(t):
    def celsius2fahrenheit(x):
        return 9 * x / 5 + 32
    result = "It's " + str(celsius2fahrenheit(t)) + " degrees!"
    return result
print(temperature(20))

print()
print('*********************************************************************************************')
print()

'''FUNCTIONS AS PARAMETERS'''


def g():
    print("Hi, it's me 'g'")
    print("Thanks for calling me")
def f(func):
    print("Hi, it's me 'f'")
    print("I will call 'func' now")
    func()
    print("by the way func's real name is " + func.__name__)
f(g)


print()
print('*********************************************************************************************')
print()

#You can also use a math function as an argument within a function
import math
def foo(func):
    print("The function " + func.__name__ + " was passed to foo")
    res = 0
    for x in [1, 2, 2.5]:
        res += func(x)
    return res
print(foo(math.sin))
print(foo(math.cos))




print()
print('*********************************************************************************************')
print()

#The output of a function is also a reference to an object. Therefore functions can return references to function objects
def f(x):
    def g(y):
        return y + x + 3
    return g

nf1 = f(1)
nf2 = f(3)

print(nf1(1))
print(nf2(1))

print()
#below is another example using a polynomial factory
def polynomial_creator(a, b, c):
    def polynomial(x):
        return a * x ** 2 + b * x + c

    return polynomial


p1 = polynomial_creator(2, 3, -1)
p2 = polynomial_creator(-1, 2, 1)

for x in range(-2, 2):
    print(x, p1(x), p2(x))

print()
print('*********************************************************************************************')
print()

def our_decorator(func):
    def function_wrapper(x):
        print("Before calling " + func.__name__)
        func(x)
        print("After calling " + func.__name__)

    return function_wrapper

def foo(x):
    print("Hi, foo has been called with " + str(x))

print("We call foo before decoration:")
foo("Hi")

print("We now decorate foo with f:")
foo = our_decorator(foo)

print("We call foo after decoration:")
foo(42)                                         #our_decorator(foo)(42)


print()
print('*********************************************************************************************')
print()

'''
You can decorate any function with @functionname immediately in front of the function you want to decorate
however, this only works when the function has only one parameter!
'''
def our_decorator(func):
    def function_wrapper(x):
        print("Before calling " + func.__name__)
        res = func(x)
        print(res)
        print("After calling " + func.__name__)
    return function_wrapper

@our_decorator                                  #create variable succ = our_decorator(succ)
def succ(n):
    return n + 1
succ(10)                                        #our_decorator(succ)(10)

print()
print('*********************************************************************************************')
print()

def argument_test_natural_number(f):
    def helper(x):
        if type(x) == int and x > 0:
            return f(x)
        else:
            raise Exception("Argument is not an integer")
    return helper

@argument_test_natural_number                   # factorial = argument_test_natural_number(factorial)
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

for i in range(1, 10):
    print(i, factorial(i))                      # i , argument_test_natural_number(factorial)(i)

print()
print('*********************************************************************************************')
print()

def call_counter(func):                         #func = succ
    def helper(x):                              #x = i
        helper.calls += 1
        return func(x)

    helper.calls = 0

    return helper

@call_counter                                   # succ = call_counter(succ)(x)
def succ(x):
    return x + 1

print(succ.calls)
for i in range(10):
    succ(i)

print(succ.calls)

print()
print('*********************************************************************************************')
print()

def evening_greeting(func):                     #func = foo
    def function_wrapper(x):                    #x = 'Hi'
        print("Good evening, " + func.__name__ + " returns:")
        func(x)
    return function_wrapper

def morning_greeting(func):
    def function_wrapper(x):
        print("Good morning, " + func.__name__ + " returns:")
        func(x)
    return function_wrapper

@evening_greeting
def foo(x):                                     #foo = evening_greeting(foo)
    print(42)

foo("Hi")                                       #evening_greeting(foo)('Hi')

print()
print('*********************************************************************************************')
print()

def greeting(expr):
    def greeting_decorator(func):               # func = foo
        def function_wrapper(x):
            print(expr + ", " + func.__name__ + " returns:")
            func(x)                             #42
        return function_wrapper
    return greeting_decorator

@greeting("καλημερα")                           # foo = greeting('καλημερα')(foo)(x)
def foo(x):
    print(42)

foo("Hi")                                       # greeting('καλημερα')(foo)('Hi')

print()
print('*********************************************************************************************')
print()

'''
__name__ (name of the function),
__doc__ (the docstring) and
__module__ (The module in which the function is defined)
'''


def greeting(func):
    def function_wrapper(x):
        """ function_wrapper of greeting """
        print("Hi, " + func.__name__ + " returns:")
        return func(x)
    function_wrapper.__name__ = func.__name__
    function_wrapper.__doc__ = func.__doc__
    function_wrapper.__module__ = func.__module__
    return function_wrapper

'''
if the above code was save as a file called 'greeting_decorator.py'
we can import the code above using the below code:
    from greeting_decorator import greeting
'''

@greeting                                   # f = greeting(f)(x)
def f(x):
    """ just some silly function """
    return x + 4

f(10)                                       # greeting(f)(10)
print("function name: " + f.__name__)
print("docstring: " + f.__doc__)
print("module name: " + f.__module__)

print()
print('*********************************************************************************************')
print()

'''
So far we used functions as decorators. Before we can define a decorator as a class, 
we have to introduce the __call__ method of classes. We mentioned alreaedy that a decorator 
is simply a callable object that takes a function as an input parameter. A function is a 
callable object, but what lots of Python programmers don't know. We can define classes as 
callable objects as well. The __call__ method is called, if the instance is called 
"like a function", i.e. using brackets.
'''

class A:
    def __init__(self):
        print("An instance of A was initialized")

    def __call__(self, *args, **kwargs):
        print("Arguments are:", args, kwargs)


x = A()
print("now calling the instance:")
x(3, 4, x=11, y=10)
print("Let's call it again:")
x(3, 4, x=11, y=10)

print()
print('*********************************************************************************************')
print()

'''
Can do the same with fib numbers
'''


class Fibonacci:
    def __init__(self):
        self.cache = {}
    def __call__(self, n):
        if n not in self.cache:
            if n == 0:
                self.cache[0] = 0
            elif n == 1:
                self.cache[1] = 1
            else:
                self.cache[n] = self.__call__(n-1) + self.__call__(n-2)
        return self.cache[n]

fib = Fibonacci()

for i in range(15):
    print(fib(i), end=", ")

print()
print('*********************************************************************************************')
print()

''' 
Using class as a decorator
'''

def decorator1(f):
    def helper():
        print("Decorating", f.__name__)
        f()
    return helper

@decorator1
def foo():
    print("inside foo()")

foo()

'''
The following decorator implemented as a class does the same "job":
'''

class decorator2:
    def __init__(self, f):
        self.f = f

    def __call__(self):
        print("Decorating", self.f.__name__)
        self.f()

@decorator2
def foo():
    print("inside foo()")


foo()