'''
The __init__ Method

We want to define the attributes of an instance right after its creation. __init__
is a method which is immediately and automatically called after an instance has been
created. This name is fixed and it is not possible to chose another name. __init__ is
one of the so-called magic methods, of which we will get to know some more details
later. The __init__ method is used to initialize an instance. There is no explicit
constructor or destructor method in Python, as they are known in C++ and Java.
The __init__ method can be anywhere in a class definition, but it is usually the first
method of a class, i.e. it follows right after the class header.
'''

class A:
    def __init__(self):
         print("__init__ has been executed!")

x = A()

print('\n************************************************************************\n')

class Robot:
    def __init__(self, name=None):
        self.name = name

    def say_hi(self):
        if self.name:
            print("Hi, I am " + self.name)
        else:
            print("Hi, I am a robot without a name")

x = Robot()
x.say_hi()
y = Robot("Marvin")
y.say_hi()