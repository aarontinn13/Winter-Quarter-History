'''
Below is an example of creating attributes for two robots (instances)
named Marvin and Caliban, with their build years being 1979 and 1993
respectively.
'''

class Robot:
    pass
x = Robot()                         #creating instance x from Robot class
y = Robot()                         #creating instance y from Robot class
x.name = "Marvin"                   #attaching arbitrary 'name' to instance x equal to 'Marvin'
x.build_year = "1979"               #attaching arbitrary 'build_year' to instance y equal to '1979'
y.name = "Caliban"                  #attaching arbitrary 'name' to instance x equal to 'Caliban'
y.build_year = "1993"               #attaching arbitrary 'build_year' to instance y equal to '1993'
print(x.name)
print(y.build_year)

print('\n****************************************************************************\n')
'''
If we look behind the scenes, the instances possess dictionaries which
they use to store attributes.
'''
print(x.__dict__)
print(y.__dict__)

print('\n****************************************************************************\n')
'''
Attributes can be assigned to class names as well. In the below case,
each instance will possess this name as well. Watch out what happens
if you assign the same name to an instance.
'''
class Robot():
    pass
x = Robot()                             #creating instance x from Robot class
Robot.brand = "Kuka"                    #attaching brand = 'Kuka' to Robot class directly
print(x.brand)                          #instance brand = class brand
x.brand = "Thales"                      #
print(Robot.brand)
y = Robot()
print(y.brand)
Robot.brand = "Thales"
print(y.brand)
print(x.brand)

print('\n****************************************************************************\n')



class Dog:
    def __init__(self, name="", height=0,weight=0):
        self.name = name
        self.height = height
        self.weight = weight

    def run(self):
        print('{} the dog runs'.format(self.name))
    def eat(self):
        print('{} the dog eats'.format(self.name))
    def bark(self):
        print('{} the dog barks'.format(self.name))

def main():
    dog1 = Dog('Spot',66,26)            #creates dog1 with following attributes under Dog class
    dog1.bark()                        #call to bark command
    dog2 = Dog()                        #creates dog2 with default attributes under Dog class
    dog2.name = 'Bowser'              #to change name attribute for dog2
    dog2.eat()                         #call dog 2 to eat command

main()


