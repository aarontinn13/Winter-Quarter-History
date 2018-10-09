class A():
    pass

a = A()
a.x = 66
a.y = "dynamically created attribute"

'''
The dictionary containing the attributes of "a" can be accessed like this:
'''

print(a.__dict__)

'''
You might have wondered that you can dynamically add attributes to the classes, 
we have defined so far, but that you can't do this with built-in classes like 
'int', or 'list':
'''

'''
x = 42
x.a = "not possible to do it"
lst = [34, 999, 1001]
lst.a = "forget it"
'''
#both above should produce an error

'''
Using a dictionary for attribute storage is very convenient, but it can mean a 
waste of space for objects, which have only a small amount of instance variables. 
The space consumption can become critical when creating large numbers of 
instances. Slots are a nice way to work around this space consumption problem. 
Instead of having a dynamic dict that allows adding attributes to objects 
dynamically, slots provide a static structure which prohibits additions after 
the creation of an instance. 

When we design a class, we can use slots to prevent the dynamic creation of 
attributes. To define slots, you have to define a list with the name __slots__. 
The list has to contain all the attributes, you want to use. We demonstrate this 
in the following class, in which the slots list contains only the name for an 
attribute "val". 
'''

class S(object):

    __slots__ = ['value']

    def __init__(self, v):
        self.value = v

x = S(42)
y = S(56)
print(x.value)
print(y.value)
#x.new = "not possible"