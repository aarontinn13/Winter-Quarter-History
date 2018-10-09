'''
Class Attributes

Obey Asimoivs Gesetzen / Gehorche Asimovs Gesetzen Instance attributes are
owned by the specific instances of a class. This means for two different
instances the instance attributes are usually different. You should by now
be familiar with this concept which we introduced the previous chapter.

We can also define attributes at the class level. Class attributes are
attributes which are owned by the class itself. They will be shared by
all the instances of the class. Therefore they have the same value for
every instance. We define class attributes outside of all the methods,
usually they are placed at the top, right below the class header.

We can see in the following interactive Python session that the class
attribute "a" is the same for all instances, in our example "x" and "y".
Besides this, we see that we can access a class attribute via an instance
or via the class name:
'''

class A:
    a = "I am a class attribute!"
x = A()
y = A()
print(x.a)
print(y.a)
print(A.a)

print('\n**********************************************************\n')
'''
But be careful, if you want to change a class attribute, you have to do it 
with the notation ClassName.AttributeName. Otherwise, you will create a new 
instance variable. We demonstrate this in the following example:
'''

class B:
    a = "I am a class attribute!"
x = B()
y = B()
x.a = "This creates a new instance attribute for x!"
print(y.a)
print(A.a)
B.a = "This is changing the class attribute 'a'!"
print(B.a)
print(y.a)
# but x.a is still the previously created instance variable:
print(x.a)

print('\n**********************************************************\n')

print(x.__dict__)
print(y.__dict__)
print(B.__dict__)
print(x.__class__.__dict__)

print('\n**********************************************************\n')

class Robot:

    Three_Laws = (
    """A robot may not injure a human being or, through inaction, allow a human being to come to harm.""",
    """A robot must obey the orders given to it by human beings, except where such orders would conflict with the First Law.,""",
    """A robot must protect its own existence as long as such protection does not conflict with the First or Second Law."""
    )

    def __init__(self, name, build_year):
        self.name = name
        self.build_year = build_year

    # other methods as usual

for number, text in enumerate(Robot.Three_Laws):
    print(str(number+1) + ":\n" + text)

print('\n**********************************************************\n')
'''
We demonstrate in the following example, how you can count instance with 
class attributes. All we have to do is
to create a class attribute, which we call "counter" in our example
to increment this attribute by 1 every time a new instance will be create
to decrement the attribute by 1 every time an instance will be destroyed
'''

class C:
    counter = 0

    def __init__(self):
        type(self).counter += 1

    def __del__(self):
        type(self).counter -= 1

if __name__ == "__main__":
    x = C()
    print("Number of instances: : " + str(C.counter))
    y = C()
    print("Number of instances: : " + str(C.counter))
    del x
    print("Number of instances: : " + str(C.counter))
    del y
    print("Number of instances: : " + str(C.counter))
    x = C()

'''
Static Methods

We used class attributes as public attributes in the previous section. 
Of course, we can make public attributes private as well. We can do this 
by adding the double underscore again. If we do so, we need a possibility 
to access and change these private class attributes. We could use instance 
methods for this purpose: 
'''

print('\n**********************************************************\n')

class Robot:
    __counter = 0

    def __init__(self):
        type(self).__counter += 1

    def RobotInstances(self):
        return Robot.__counter

if __name__ == "__main__":
    x = Robot()
    print('Number of Instances: ', x.RobotInstances())
    y = Robot()
    print('Number of Instances: ', x.RobotInstances())

print('\n**********************************************************\n')
'''
The call "x.RobotInstances()" is treated as an instance method call and 
an instance method needs a reference to the instance as the first parameter. 

So, what do we want? We want a method, which we can call via the class 
name or via the instance name without the necessity of passing a reference 
to an instance to it. 

The solution consists in static methods, which don't need a reference to 
an instance. 
It's easy to turn a method into a static method. All we have to do is to 
add a line with "@staticmethod" directly in front of the method header. It's 
the decorator syntax. 

You can see in the following example that we can now use our method 
RobotInstances the way we wanted: 
'''


class Robot:
    __counter = 0

    def __init__(self):
        type(self).__counter += 1

    @staticmethod
    def RobotInstances():
        return Robot.__counter

if __name__ == "__main__":
    print(Robot.RobotInstances())   #print 0
    x = Robot()                     #increase counter by 1
    print(x.RobotInstances())       #print 1
    y = Robot()                     #increase counter by 1
    print(x.RobotInstances())       #print 2
    print(y.RobotInstances())       #print 2
    print(Robot.RobotInstances())   #print 2

print('\n**********************************************************\n')

'''
Class Methods

Static methods shouldn't be confused with class methods. Like static methods 
class methods are not bound to instances, but unlike static methods class 
methods are bound to a class. The first parameter of a class method is a 
reference to a class, i.e. a class object. They can be called via an instance 
or the class name. 
'''


class Robot:
    __counter = 0

    def __init__(self):
        type(self).__counter += 1

    @classmethod
    def RobotInstances(cls):
        return cls, Robot.__counter

if __name__ == "__main__":
    print(Robot.RobotInstances())
    x = Robot()
    print(x.RobotInstances())
    y = Robot()
    print(x.RobotInstances())
    print(Robot.RobotInstances())

print('\n**********************************************************\n')
'''
The use cases of class methods:

the are used in the definition of the so-called factory methods, which we will 
not cover here.
They are often used, where we have static methods, which have to call other 
static methods. To do this, we would have to hard code the class name, if we 
had to use static methods. This is a problem, if we are in a use case, where 
we have inherited classes.

The following program contains a fraction class, which is still not complete. 
If you work with fractions, you need to be capable of reducing fractions, e.g. 
the fraction 8/24 can be reduced to 1/3. We can reduce a fraction to lowest 
terms by dividing both the numerator and denominator by the Greatest Common 
Divisor (GCD). 

We have defined a static gcd function to calculate the greatest common divisor 
of two numbers. the greatest common divisor (gcd) of two or more integers 
(at least one of which is not zero), is the largest positive integer that 
divides the numbers without a remainder. For example, the 'GCD of 8 and 24 
is 8. The static method "gcd" is called by our class method "reduce" with 
"cls.gcd(n1, n2)". "CLS" is a reference to "fraction". 
'''

class fraction(object):
    def __init__(self, n, d):
        self.numerator = fraction.reduce(n, d)
        self.denominator = fraction.reduce(n, d)

    @staticmethod
    def gcd(a, b):              #8, 24
        while b != 0:           #while 24 does not = 0
            a, b = b, a % b     #first_iteration = 24,8...second_iteration = 8,0
        return a

    @classmethod
    def reduce(cls, n1, n2):
        g = cls.gcd(n1, n2)
        return (n1 // g, n2 // g)

    def __str__(self):
        return str(self.numerator) + '/' + str(self.denominator)

x = fraction(8,24)
print(x)

print('\n**********************************************************\n')
'''
We will demonstrate in our last example the usefulness of class methods in 
inheritance. We define a class "Pets" with a method "about". This class will 
be inherited in a subclass "Dogs" and "Cats". The method "about" will be 
inherited as well. We will define the method "about" as a "staticmethod" in 
our first implementation to show the disadvantage of this approach:
'''


class Pets:
    name = "pet animals"

    @staticmethod
    def about():
        print("This class is about {}!".format(Pets.name))

class Dogs(Pets):
    name = "'man's best friends' (Frederick II)"

class Cats(Pets):
    name = "cats"

p = Pets()
p.about()
d = Dogs()
d.about()
c = Cats()
c.about()
print(Pets.name)
print(Dogs.name)
print(Cats.name)

print('\n**********************************************************\n')
'''
Especially, in the case of c.about() and d.about(), we would have preferred a more 
specific phrase! The "problem" is that the method "about" doesn't know that it has 
been called by an instance of the Dogs or Cats class. 

We decorate it now with a classmethod decorator instead of a staticmethod decorator:
'''

class Pets:
    name = "pet animals"

    @classmethod
    def about(cls):
        print("This class is about {}!".format(cls.name))

class Dogs(Pets):
    name = "'man's best friends' (Frederick II)"

class Cats(Pets):
    name = "cats"

p = Pets()
p.about()

d = Dogs()
d.about()

c = Cats()
c.about()

print('\n**********************************************************\n')
'''
An example from Stack overflow...
'''

class A(object):
    def foo(self,x):
        print("executing foo(%s,%s)"%(self,x))

    @classmethod
    def class_foo(cls,x):
        print("executing class_foo(%s,%s)"%(cls,x))

    @staticmethod
    def static_foo(x):
        print("executing static_foo(%s)"%x)

a=A()

'''
Below is the usual way an object instance calls a method. The object instance, a, 
is implicitly passed as the first argument.
'''
print('calling: a.foo(1)')
a.foo(1)

'''
With classmethods, the class of the object instance is implicitly passed as the 
first argument instead of self.
'''
print('\ncalling: a.class_foo(1)')
a.class_foo(1)

'''
You can also call class_foo using the class. In fact, if you define something to 
be a classmethod, it is probably because you intend to call it from the class 
rather than from a class instance. A.foo(1) would have raised a TypeError, but 
A.class_foo(1) works just fine:
'''
print('\ncalling: A.class_foo(1)')
A.class_foo(1)

'''
One use people have found for class methods is to create inheritable alternative 
constructors.

With staticmethods, neither self (the object instance) nor  cls (the class) is 
implicitly passed as the first argument. They behave like plain functions except 
that you can call them from an instance or the class:
'''
print('\ncalling: a.static_foo(1)')
a.static_foo(1)
print('\ncalling: A.static_foo(\'hi\')')
A.static_foo('hi')

'''
Staticmethods are used to group functions which have some logical connection with 
a class to the class.

foo is just a function, but when you call a.foo you don't just get the function, 
you get a "partially applied" version of the function with the object instance a 
bound as the first argument to the function. foo expects 2 arguments, while a.foo 
only expects 1 argument.

a is bound to foo. That is what is meant by the term "bound" below:
'''
print('\ncalling: print(a.foo)')
print(a.foo)

'''
With a.class_foo, a is not bound to class_foo, rather the class A is bound to class_foo.
'''
print('\ncalling: print(a.class_foo)')
print(a.class_foo)

'''
Here, with a staticmethod, even though it is a method, a.static_foo just returns 
a good 'ole function with no arguments bound. static_foo expects 1 argument, and 
a.static_foo expects 1 argument too.
'''
print('\ncalling: print(a.static_foo)')
print(a.static_foo)

'''
And of course the same thing happens when you call static_foo with the class A instead.
'''
print('\ncalling: print(A.static_foo)')
print(A.static_foo)
