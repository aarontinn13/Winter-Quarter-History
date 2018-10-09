'''
The "diamond problem" (sometimes referred to as the "deadly diamond of death") is the
generally used term for an ambiguity that arises when two classes B and C inherit from
a superclass A, and another class D inherits from both B and C. If there is a method
"m" in A that B or C (or even both of them) )has overridden, and furthermore, if does
not override this method, then the question is which version of the method does D inherit?
It could be the one from A, B or C

Let's look at Python. The first Diamond Problem configuration is like this: Both B and C
override the method m of A:
                                            A
                                           / \
                                          /   \
                                         B     C
                                          \   /
                                           \ /
                                            D
'''

class A:
    def m(self):
        print("m of A called")

class B(A):
    def m(self):
        print("m of B called")

class C(A):
    def m(self):
        print("m of C called")

class D(C,B):                   #switch the order of C, B to B, C to achieve different results
    pass

'''
If you call the method m on an instance x of D, i.e. x.m(), we will get the output 
"m of B called". If we transpose the order of the classes in the class header of D in 
"class D(C,B):", we will get the output "m of C called". 

The case in which m will be overridden only in one of the classes B or C, e.g. in C: 
'''

x = D()
x.m()

print('\n*********************************************************************\n')
'''
We have seen in our previous implementation of the diamond problem, how Python "solves" 
the problem, i.e. in which order the base classes are browsed through. The order is defined 
by the so-called "Method Resolution Order" or in short MRO.1\ 

We will extend our previous example, so that every class defines its own method m: 
'''

class A:
    def m(self):
        print("m of A called")

class B(A):
    def m(self):
        print("m of B called")

class C(A):
    def m(self):
        print("m of C called")

class D(B, C):
    def m(self):
        print("m of D called")

x = D()
B.m(x)
C.m(x)
A.m(x)

'''
Now let's assume that the method m of D should execute the code of m of B, C and A as 
well, when it is called. We could implement it like this: 
'''

print('\n*********************************************************************\n')
class D(B,C):
    def m(self):
        print("m of D called")
        B.m(self)
        C.m(self)
        A.m(self)

x = D()
x.m()


print('\n*********************************************************************\n')
'''
But it turns out once more that things are more complicated than it seems. How can we 
cope with the situation, if both m of B and m of C will have to call m of A as well. 
In this case, we have to take away the call A.m(self) from m in D. The code might look 
like this, but there is still a bug lurking in it: 

The bug is that the method m of A will be called twice: 
'''


class A:
    def m(self):
        print("m of A called")

class B(A):
    def m(self):
        print("m of B called")
        A.m(self)

class C(A):
    def m(self):
        print("m of C called")
        A.m(self)

class D(B, C):
    def m(self):
        print("m of D called")
        B.m(self)
        C.m(self)
x = D()
x.m()

print('\n*********************************************************************\n')

'''
One way to solve this problem - admittedly not a Pythonic one - consists in splitting 
the methods m of B and C in two methods. The first method, called _m consists of the 
specific code for B and C and the other method is still called m, but consists now of 
a call "self._m()" and a call "A.m(self)". The code of the method m of D consists now 
of the specific code of D 'print("m of D called")', and the calls B._m(self), C._m(self) 
and A.m(self): 
'''
class A:
    def m(self):
        print("m of A called")

class B(A):
    def _m(self):
        print("m of B called")

    def m(self):
        self._m()
        A.m(self)

class C(A):
    def _m(self):
        print("m of C called")

    def m(self):
        self._m()
        A.m(self)

class D(B, C):
    def m(self):
        print("m of D called")
        B._m(self)
        C._m(self)
        A.m(self)

print('\n*********************************************************************\n')
'''
The optimal way to solve the problem, which is the "super" pythonic way, consists in 
calling the super function: 
'''


class A:
    def m(self):
        print("m of A called")


class B(A):
    def m(self):
        print("m of B called")
        super().m()


class C(A):
    def m(self):
        print("m of C called")
        super().m()


class D(B, C):
    def m(self):
        print("m of D called")
        super().m()

x = D()
x.m()

print('\n*********************************************************************\n')
'''
The super function is often used when instances are initialized with the __init__ method: 
'''


class A:
    def __init__(self):
        print("A.__init__")


class B(A):
    def __init__(self):
        print("B.__init__")
        super().__init__()


class C(A):
    def __init__(self):
        print("C.__init__")
        super().__init__()

class D(B, C):
    def __init__(self):
        print("D.__init__")
        super().__init__()

d = D()
print()
c = C()
print()
b = B()
print()
a = A()

'''
The question arises how the super functions makes its decision. How does it decide 
which class has to be used? As we have already mentioned, it uses the so-called method 
resolution order(MRO). It is based on the "C3 superclass linearisation" algorithm. 
This is called a linearisation, because the tree structure is broken down into a linear 
order. The mro method can be used to create this list: 
'''
print(D.mro())
print(B.mro())
print(A.mro())