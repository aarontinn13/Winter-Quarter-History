'''

Who doesn't know those trigger-happy farmers from films. Shooting as soon as somebody
enters their property. This "somebody" has of course neglected the "no trespassing"
sign, indicating that the land is private property. Maybe he hasn't seen the sign,
maybe the sign is hard to be seen? Imagine a jogger, running the same course five times
a week for more than a year, but than he receives a $50 fine for trespassing in the
Winchester Fells. Trespassing is a criminal offence in Massachusetts. He was innocent
anyway, because the signage was inadequate in the area.4

Even though no trespassing signs and strict laws do protect the private property, some
surround their property with fences to keep off unwanted "visitors". Should the fence
keep the dog in the yard or the burglar in the street? Choose your fence: Wood panel
fencing, post-and-rail fencing, chain-link fencing with or without barbed wire and so on.

We have a similar situation in the design of object-oriented programming languages.
The first decision to take is how to protect the data which should be private. The second
decision is what to do if trespassing, i.e. accessing or changing private data, occurs.
Of course, the private data may be protected in a way that it can't be accessed under
no circumstances. This is hardly possible in practice, as we know from the old saying
"Where there's a will, there's a way"!

Enter at your own risk Some owners allow a restricted access to their property. Joggers
or hikers may find signs like "Enter at your own risk". A third kind of property might
be public property like streets or parks, where it is perfectly legal to be.

We have the same classification again in object-oriented programming:

-Private attributes should only be used by the owner, i.e. inside of the class definition
itself.

-Protected (restricted) Attributes may be used, but at your own risk. Essentially, this
means that they should only be used under certain conditions.

-Public Attributes can and should be freely used.

Python uses a special naming scheme for attributes to control the accessibility of the
attributes. So far, we have used attribute names, which can be freely used inside or
outside of a class definition, as we have seen. This corresponds to public attributes
of course.

There are two ways to restrict the access to class attributes:
First, we can prefix an attribute name with a leading underscore "_". This marks the
attribute as protected. It tells users of the class not to use this attribute unless,
somebody writes a subclass. We will learn about inheritance and subclassing in the next
chapter of our tutorial.
Second, we can prefix an attribute name with two leading underscores "__". The attribute
is now inaccessible and invisible from outside. It's neither possible to read nor write
to those attributes except inside of the class definition itself.
'''

class A():
    def __init__(self):
        self.__priv = "I am private"
        self._prot = "I am protected"
        self.pub = "I am public"
x = A()
print(x.pub)
print(x._prot)
#print(x.__priv) #will product error

print('\n************************************************************************\n')

class Robot:
    def __init__(self, name=None, build_year=2000):
        self.__name = name
        self.__build_year = build_year

    def say_hi(self):
        if self.__name:
            print("Hi, I am " + self.__name)
        else:
            print("Hi, I am a robot without a name")

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_build_year(self, by):
        self.__build_year = by

    def get_build_year(self):
        return self.__build_year

    def __repr__(self):
        return "Robot('" + self.__name + "', " + str(self.__build_year) + ")"

    def __str__(self):
        return "Name: " + self.__name + ", Build Year: " + str(self.__build_year)


if __name__ == "__main__":
    x = Robot("Marvin", 1979)
    y = Robot("Caliban", 1943)
    for rob in [x, y]:
        rob.say_hi()
        if rob.get_name() == "Caliban":
            rob.set_build_year(1993)
        print("I was built in the year " + str(rob.get_build_year()) + "!")