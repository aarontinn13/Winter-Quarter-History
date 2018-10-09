
#DOC STRING, returns the string in the first line in the function
def Hello(name="everybody"):
    """ Greets a person """
    print("Hello " + name + "!")
print("The docstring of the function Hello: " + Hello.__doc__)

#multiple variables
def sumsub(a, b, c=0, d=0):
    return a - b + c - d
print(sumsub(12,4))
print(sumsub(42,15,d=10))   #same as below
print(sumsub(42,15,0,10))   #same as above

#returning something
def return_sum(x,y):
    c = x + y
    return c
res = return_sum(4,5)
print(res)

#Try function to test if pi is a float
float_pi = "3.14"
def isfloat(str_val):
    try:
        float(str_val)
        return True
    except ValueError:
        return False
print("Is pi a Float: ", isfloat(float_pi))


#basic function below

def add_numbers(num1, num2):
    return num1 + num2

print("5 + 4 = ", add_numbers(5, 4))





#Optional parameters
def Hello(name="everybody"):
    """ Greets a person """
    print("Hello " + name + "!")
Hello("Peter")
Hello()             #if nothing is entered, default is 'everybody'



#returning multiple values
def fib_intervall(x):
    """ returns the largest fibonacci
    number smaller than x and the lowest
    fibonacci number higher than x"""
    if x < 0:
        return -1
    (old, new, lub) = (0, 1, 0)
    while True:
        if new < x:
            lub = new
            (old, new) = (new, old + new)
        else:
            return (lub, new)
while True:
    x = int(input("Your number: "))
    if x <= 0:
        break
    (lub, sup) = fib_intervall(x)
    print("Largest Fibonacci Number smaller than x: " + str(lub))
    print("Smallest Fibonacci Number larger than x: " + str(sup))




#solve for x
#x + 4 = 9

def solve_eq(equation):
    x, add, num1, equal, num2 = equation.split()
    num1, num2 = int(num1), int(num2)
    print("x = " + str(num2 - num1))

solve_eq("x + 4 = 9")





#how to return multiple values

def mult_divide(num1, num2):
    return (num1 * num2), (num1 / num2)

mult, divide = mult_divide(5, 4)

print('5 * 4 = ', mult)
print('5 / 4 = ', divide)


# create all prime numbers from 1 - x
def isprime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True

def getprime(max):
    listofprimes = []
    for num1 in range(2, max):
        if isprime(num1):
            listofprimes.append(num1)
    return listofprimes

max = int(input('What is the max Prime? '))
listofprimes = getprime(max)
for prime in listofprimes:
    print(prime)

