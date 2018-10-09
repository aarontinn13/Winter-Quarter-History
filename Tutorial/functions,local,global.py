#You can access an outside variable from inside a function
def f():
    print(s)
s = "I love Paris in the summer!"
f()

print()

#however, you cannot access a local variable from outside of the function.
def f():
    s = "I am globally not known"
    print(s)

f()
print(s)

print()

#can change the value of s inside of the variable but does not affect outside variable
def f():
    s = "I love London!"
    print(s)
s = "I love Paris!"
f()
print(s)

print()

#if we call for outside varible s and create local variable s, python doesn't like that
'''
def f():
    print(s)
    s = "I love London!"
    print(s)

s = "I love Paris!"
f()
'''

#once we make s global, we can change and call inside or outside a function and will have global effect
def f():
    global s
    print(s)
    s = "Only in spring, but London is great as well!"
    print(s)
s = "I am looking for a course in Paris!"
f()
print(s)

print()

#below is a mix of everything we learned of accessing and changing inside and outside functions
def foo(x, y):                  #x = 17, y = 4
    global a                    #global a
    a = 42                      #a changes from 1 to 42
    x,y = y,x                   #x = 4 , y = 17
    b = 33                      #change b to 33
    b = 17                      #change b to 17
    c = 100                     #create c = 100

    print(a,b,x,y)

a, b, x, y = 1, 15, 3, 4
foo(17, 4)
print(a, b, x, y)

print()



#global variables inside nested functions A variable defined inside of a function is local unless it is explicitly marked as global.
def f():

    x = 42
    def g():
        global x
        x = 43
        print('Inside of g function: ', str(x))
    print("Before calling g: " + str(x))
    g()
    print("After calling g: " + str(x))

x = 41
print('Before calling any functions: ', str(x))
f()
print("x in main: " + str(x))

x = None

print()


#non local variables
def f():
    x = 42
    def g():
        nonlocal x
        x = 43
    print("Before calling g: " + str(x))
    print("Calling g now:")
    g()
    print("After calling g: " + str(x))
x = 41
f()
print("x in main: " + str(x))


