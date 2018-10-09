'''
Getters and setters are used in many object oriented programming languages to
ensure the principle of data encapsulation. They are known as mutator methods
as well. Data encapsulation - as we have learnt in our introduction on Object
Oriented Programming of our tutorial - is seen as the bundling of data with
the methods that operate on these data. These methods are of course the getter
for retrieving the data and the setter for changing the data. According to
this principle, the attributes of a class are made private to hide and protect
them from other code.

Unfortunately, it is widespread belief that a proper Python class should
encapsulate private attributes by using getters and setters. As soon as one of
these programmers introduces a new attribute, he or she will make it a private
variable and creates "automatically" a getter and a setter for this attributes.
Such programmers may even use an editor or an IDE, which automatically create
getters and setters for all private attributes. These tools even warn the
programmer if she or he uses a public attribute! Java programmers will wrinkle
their brows, screw up their noses, or even scream with horror when they read
the following: The Pythonic way to introduce attributes is to make them public.

We will explain this later. First, we demonstrate in the following example, how
 we can design a class in a Javaesque way with getters and setters to encapsulate
 the private attribute "self.__x":
'''

class P:

    def __init__(self,x):
        self.__x = x

    def get_x(self):
        return self.__x

    def set_x(self, x):
        self.__x = x

p1 = P(42)
p2 = P(4711)
print(p1.get_x())
p1.set_x(47)
p1.set_x(p1.get_x()+p2.get_x())
print(p1.get_x())

print('\n*****************************************************************\n')
'''
The above expression is very ugly i.e. (p1.set_x(p1.get_x()+p2.get_x()))
We could remove the set and get functions and make x public so we can type:
p1.x = p1.x + p2.x 

"But, but, but, but, but ... ", we can hear them howling and screaming, "But 
there is NO data ENCAPSULATION!" 
Yes, in this case there is no data encapsulation. We don't need it in this 
case. The only thing get_x and set_x in our starting example did was "getting 
the data through" without doing anything, no checks nothing. 

But what happens if we want to change the implementation in the future. This 
is a serious argument. Let's assume we want to change the implementation like 
this: The attribute x can have values between 0 and 1000. If a value larger 
than 1000 is assigned, x should be set to 1000. Correspondingly, x should be 
set to 0, if the value is less than 0. 

It is easy to change our first P class to cover this problem. We change the 
set_x method accordingly:
'''

class P:

    def __init__(self,x):
        self.set_x(x)

    def get_x(self):
        return self.__x

    def set_x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x

p1 = P(99999999999)
print(p1.get_x())

p2 = P(500)
print(p2.get_x())

p3 = P(-999999999999)
print(p3.get_x())

print('\n*****************************************************************\n')
'''
Our new class means breaking the interface. The attribute x is not available 
anymore. That's why in Java e.g. people are recommended to use only private 
attributes with getters and setters, so that they can change the implementation 
without having to change the interface. 

But Python offers a solution to this problem. The solution is called properties! 

The class with a property looks like this:
'''

class P:

    def __init__(self,y):
        print('1st')
        self.y = y

    @property
    def y(self):                        #property(x)(self):
        print('3rd')
        return self.__x

    @y.setter                           #does this automatically run when an instance is created?
    def y(self, x):
        print('2nd')
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x

'''
A method which is used for getting a value is decorated with "@property", i.e. 
we put this line directly in front of the header. The method which has to function 
as the setter is decorated with "@x.setter". If the function had been called "f", 
we would have to decorate it with "@f.setter". 

Two things are noteworthy: We just put the code line "self.x = x" in the 
__init__ method and the property method x is used to check the limits of the 
values. The second interesting thing is that we wrote "two" methods with the 
same name and a different number of parameters "def x(self)" and "def x(self,x)". 
We have learned in a previous chapter of our course that this is not possible. 
It works here due to the decorating:
'''

p1 = P(99999)
print(p1.y)
p1.y = -99999
print(p1.y)

print('\n*****************************************************************\n')
'''
Alternatively, we could have used a different syntax without decorators to define 
the property. As you can see, the code is definitely less elegant and we have to 
make sure that we use the getter function in the __init__ method again: 
'''

class P:

    def __init__(self,x):
        print('1st')
        self.set_x(x)

    def get_x(self):
        print('3rd')
        return self.__x

    def set_x(self, x):
        print('2nd')
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x

    x = property(get_x)

p1 = P(5)
print(p1.x)


print('\n*****************************************************************\n')

'''

There is still another problem in the most recent version. We have now two ways 
to access or change the value of x: Either by using "p1.x = 42" or by "p1.set_x(42)". 
This way we are violating one of the fundamentals of Python: "There should be one-- 
and preferably only one --obvious way to do it." (see Zen of Python) 

We can easily fix this problem by turing the getter and the setter method into private 
methods, which can't be accessed anymore by the users of our class P:
'''
class P:

    def __init__(self,x):
        print('1st')
        self.__set_x(x)

    def __get_x(self):
        print('3rd')
        return self.__x

    def __set_x(self, x):
        print('2nd')
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x

    x = property(__get_x)

p1 = P(5)
print(p1.x)

print('\n*****************************************************************\n')
'''
The following example shows a class, which has internal attributes, which can't be 
accessed from outside. These are the private attributes self.__potential_physical 
and self.__potential_psychic. Furthermore we show that a property can be deduced 
from the values of more than one attribute. The property "condition" of our example 
returns the condition of the robot in a descriptive string. The condition depends 
on the sum of the values of the psychic and the physical conditions of the robot. 
'''


class Robot:
    def __init__(self, name, build_year, lk=0.5, lp=0.5):
        self.name = name
        self.build_year = build_year
        self.__potential_physical = lk
        self.__potential_psychic = lp


    def condition(self):
        s = self.__potential_physical + self.__potential_psychic
        if s <= -1:
            return "I feel miserable!"
        elif s <= 0:
            return "I feel bad!"
        elif s <= 0.5:
            return "Could be worse!"
        elif s <= 1:
            return "Seems to be okay!"
        else:
            return "Great!"

if __name__ == "__main__":
    x = Robot("Marvin", 1979, 0.2, 0.4)
    y = Robot("Caliban", 1993, -0.4, 0.3)
    print(x.condition)
    print(y.condition)