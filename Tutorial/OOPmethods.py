'''
We want to demonstrate now, how we can define methods in classes.

Methods in Python are essentially functions in accordance with Guido's
saying "first-class everything".

Let's define a function "hi", which takes an object "obj" as an
argument and assumes that this object has an attribute "name". We will
also define again our basic Robot class:
'''

def hi(obj):
    print("Hi, I am " + obj.name + "!")

class Robot:
    pass

x = Robot()
x.name = "Marvin"
hi(x)

print('\n***********************************************************************\n')


def hi(obj):
    print("Hi, I am " + obj.name)


class Robot:
    say_hi = hi


x = Robot()
x.name = "Marvin"
Robot.say_hi(x)

'''
"say_hi" is called a method. Usually, it will be called like this: 

x.say_hi() 

It is possible to define methods like this, but you shouldn't do it. 

The proper way to do it:
Instead of defining a function outside of a class definition and binding 
it to a class attribute, we define a method directly inside (indented) 
of a class definition.
A method is "just" a function which is defined inside of a class.
The first parameter is used a reference to the calling instance.
This parameter is usually called self.
Self corresponds to the Robot object x.


We have seen that a method differs from a function only in two aspects:
It belongs to a class, and it is defined within a class
The first parameter in the definition of a method has to be a reference 
to the instance, which called the method. This parameter is usually called "self".
As a matter of fact, "self" is not a Python keyword. It's just a naming 
convention! So C++ or Java programmers are free to call it "this", but 
this way they are risking that others might have greater difficulties 
in understanding their code! 

Most other object-oriented programming languages pass the reference to the 
object (self) as a hidden parameter to the methods. 

You saw before that the calls Robot.say_hi(x)". and "x.say_hi()" are 
equivalent. "x.say_hi()" can be seen as an "abbreviated" form, i.e. Python 
automatically binds it to the instance name. Besides this "x.say_hi()" is 
the usual way to call methods in Python and in other object oriented languages. 

For a Class C, an instance x of C and a method m of C the following three 
method calls are equivalent:

type(x).m(x, ...)
C.m(x, ...)
x.m(...)

Before you proceed with the following text, you may mull over the previous 
example for awhile. Can you figure out, what is wrong in the design? 

There is more than one thing about this code, which may disturb you, but the 
essential problem at the moment is the fact that we create a robot and that 
after the creation, we shouldn't forget about naming it! If we forget it, say_
hi will raise an error. 

We need a mechanism to initialize an instance right after its creation. This 
is the __init__-method, which we cover in the next section. 
'''