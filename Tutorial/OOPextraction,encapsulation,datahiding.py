'''
Definitions of Terms:

Data Abstraction, Data Encapsulation and Information Hiding are often synonymously
used in books and tutorials on OOP. But there is a difference.

Encapsulation is seen as the bundling of data with the methods that operate on that
data.

Information hiding on the other hand is the principle that some internal
information or data is "hidden", so that it can't be accidentally changed.

Data encapsulation via methods doesn't necessarily mean that the data is hidden.
You might be capable of accessing and seeing the data anyway, but using the methods
is recommended. Finally, data abstraction is present, if both data hiding and data
encapsulation is used. This means data abstraction is the broader term:

Data Abstraction = Data Encapsulation + Data Hiding

Encapsulation is often accomplished by providing two kinds of methods for attributes:
The methods for retrieving or accessing the values of attributes are called getter methods.
Getter methods do not change the values of attributes, they just return the values.
The methods used for changing the values of attributes are called setter methods.

We will define now a Robot class with a Getter and a Setter for the name attribute. We will
call them get_name and set_name accordingly.
'''


class Robot:
    def __init__(self, name=None):
        self.name = name

    def say_hi(self):
        if self.name:
            print("Hi, I am " + self.name)
        else:
            print("Hi, I am a robot without a name")

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name


x = Robot()
x.set_name("Henry")
x.say_hi()
y = Robot()
y.set_name(x.get_name())
print(y.get_name())
y.say_hi()

print('\n**********************************************************************\n')


class Robot:
    def __init__(self, name=None, build_year=None):
        self.name = name
        self.build_year = build_year

    def say_hi(self):
        if self.name:
            print("Hi, I am " + self.name)
        else:
            print("Hi, I am a robot without a name")
        if self.build_year:
            print("I was built in " + str(self.build_year))
        else:
            print("It's not known, when I was created!")

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_build_year(self, by):
        self.build_year = by

    def get_build_year(self):
        return self.build_year


x = Robot("Henry", 2008)
y = Robot()
y.set_name("Marvin")
x.say_hi()
y.say_hi()


print('\n**********************************************************************\n')

l = ["Python", "Java", "C++", "Perl"]
print(l)
print(str(l))
print(repr(l))
d = {"a":3497, "b":8011, "c":8300}
print(d)
print(str(d))
print(repr(d))
x = 587.78
print(str(x))
print(repr(x))

print('\n**********************************************************************\n')
'''
If you apply str or repr to an object, Python is looking for a corresponding method 
__str__ or __repr__ in the class definition of the object. If the method does exist, 
it will be called. 
In the following example, we define a class A, having neither a __str__ nor a __repr__ 
method. We want to see, what happens, if we use print directly on an instance of this 
class, or if we apply str or repr to this instance: 
'''

class A:
    pass

a = A()
print(a)
print(repr(a))
print(str(a))
print(a)

print('\n**********************************************************************\n')

class B:
    def __str__(self):
        return "42"

b = B()
print(repr(b))
print(str(b))
print(b)

print('\n**********************************************************************\n')

class C:
    def __repr__(self):
        return "42"
a = A()
print(repr(a))
print(str(a))
print(a)

print('\n**********************************************************************\n')

'''
o == eval(repr(o)) 
This is shown in the following interactive Python session:
'''

l = [3,8,9]
s = repr(l)
print(s)
print(l == eval(s))
print(l == eval(str(l)))

print('\n**********************************************************************\n')

import datetime
today = datetime.datetime.now()
str_s = str(today)
#eval(str_s) #gives error
repr_s = repr(today)
t = eval(repr_s)
print(type(t))

print('\n**********************************************************************\n')

'''
We can see that eval(repr_s) returns again a datetime.datetime object. The String 
created by str can't be turned into a datetime.datetime object by parsing it. 

We will extend our robot class with a repr method. We dropped the other methods to 
keep this example simple: 
'''

class Robot:
    def __init__(self, name, build_year):
        self.name = name
        self.build_year = build_year

    def __repr__(self):
        return "Robot('" + self.name + "', " + str(self.build_year) + ")"

if __name__ == "__main__":
    x = Robot("Marvin", 1979)
    x_str = str(x)
    print(x_str)
    print("Type of x_str: ", type(x_str))
    new = eval(x_str)
    print(new)
    print("Type of new:", type(new))

print('\n**********************************************************************\n')

class Robot2:
    def __init__(self, name, build_year):
        self.name = name
        self.build_year = build_year

    def __repr__(self):
        return "Robot(\"" + self.name + "\"," + str(self.build_year) + ")"

    def __str__(self):
        return "Name: " + self.name + ", Build Year: " + str(self.build_year)


if __name__ == "__main__":
    x = Robot2("Marvin", 1979)
    x_repr = repr(x)
    print(x_repr, type(x_repr))
    new = eval(x_repr)
    print(new)
    print("Type of new:", type(new))