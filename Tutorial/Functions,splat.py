#If we do not know how many positional parameters we will pass through the function we can use *to denote as many arguments
def sumAll(*args):
    sum = 0
    for i in args:
        sum += i
    return sum
print('The sum is: ', sumAll(1,2,3,4,5,6,7))

#If we are dealing with a list, we must use splat when calling for that list to 'unpack the list. In this case we are going to unpack 5 different variables to place inside of *args
list = [1,2,3,4,5]
def f(*args):
    x = 0
    for i in args:
        x = x + i
    return x
print('The sum of the iteration is: ', f(*list))

#for keyword parameters we need double asterick

def f(**kwargs):
    print(kwargs)
f()
f(de="German",en="English",fr="French")

#OR

def f(**a):
    print(a)
d = {'a':'append', 'b':'block','x':'extract','y':'yes'}
f(**d)






print()
print('***************************************************************************************')





#get the area of a circle or rectangle

import math

def get_area(shape):
    shape = shape.lower()

    if shape =="rectangle":
        rectangle_area()
    elif shape == "circle":
        circle_area()
    elif shape == "square":
        square()
    else:
        print("Please enter rectangle, circle or square!")

def square():
    side = float(input('Enter the side length: '))

    area = math.pow(side,2)

    print('The area of the square is: ', area)

def rectangle_area():
    length = float(input('Enter the length: '))
    width = float(input('Enter the width: '))

    area = length * width

    print('The area of the rectangle is: {:.0f}'.format(area))

def circle_area():
    radius = float(input('Enter the radius: '))

    area = math.pi * (math.pow(radius, 2))

    print('The area of the circle is {:.2f}'.format(area))

def main():
    shape_type = input('Get area for what shape: ')
    get_area(shape_type)

main()

