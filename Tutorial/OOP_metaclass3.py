'''
After you have hopefully gone through our chapter Introduction into Metaclasses you
may have asked yourself about possible use cases for metaclasses. There are some
interesting use cases and it's not - like some say - a solution waiting for a
problem. We have mentioned already some examples.

In this chapter of our tutorial on Python, we want to elaborate an example metaclass,
which will decorate the methods of the subclass. The decorated function returned by
the decorator makes it possible to count the number of times each method of the
subclass has been called.

This is usually one of the tasks, we expect from a profiler. So we can use this
metaclass for simple profiling purposes. Of course, it will be easy to extend our
metaclass for further profiling tasks.

Before we actually dive into the problem, we want to call to mind again how we can
access the attributes of a class. We will demonstrate this with the list class. We
can get the list of all the non private attributes of a class - in our example the
random class - with the following construct:
'''

import random
cls = "random" # name of the class as a string
all_attributes = [x for x in dir(eval(cls)) if not x.startswith("__") ]
print(all_attributes)

print('\n************************************************************************************************\n')
#Now, we are filtering the callable attributes, i.e. the public methods of the class.

methods = [x for x in dir(eval(cls)) if not x.startswith("__")
                              and callable(eval(cls + "." + x))]
print(methods)

print('\n************************************************************************************************\n')
'''
Getting the non callable attributes of the class can be easily achieved by negating callable, i.e. adding "not":
'''

non_callable_attributes = [x for x in dir(eval(cls)) if not x.startswith("__")
                              and not callable(eval(cls + "." + x))]
print(non_callable_attributes)

print('\n************************************************************************************************\n')

'''
In normal Python programming it is neither recommended nor necessary to apply methods in the following way, but it
is possible:
'''

lst = [3,4]
list.__dict__["append"](lst, 42)
print(lst)

print('\n************************************************************************************************\n')
'''
A Decorator for Counting Function Calls

Finally, we will begin to design the metaclass, which we have mentioned as our target in the beginning of this 
chapter. It will decorate all the methods of its subclass with a decorator, which counts the number of calls. We 
have defined such a decorator in our chapter Memoization and Decorators:
'''

def call_counter(func):
    def helper(*args, **kwargs):
        helper.calls += 1
        return func(*args, **kwargs)
    helper.calls = 0
    helper.__name__= func.__name__
    return helper

@call_counter
def f():
    pass

print(f.calls)
for _ in range(10):
    f()

print(f.calls)


print('\n************************************************************************************************\n')
'''
The "Count Calls" Metaclass

Now we have all the necessary "ingredients" together to write our metaclass. We will include our call_counter 
decorator as a staticmethod:
'''


class FuncCallCounter(type):
    """ A Metaclass which decorates all the methods of the
        subclass using call_counter as the decorator
    """

    @staticmethod
    def call_counter(func):
        """ Decorator for counting the number of function
            or method calls to the function or method func
        """

        def helper(*args, **kwargs):
            helper.calls += 1
            return func(*args, **kwargs)

        helper.calls = 0
        helper.__name__ = func.__name__

        return helper

    def __new__(cls, clsname, superclasses, attributedict):
        """ Every method gets decorated with the decorator call_counter,
            which will do the actual call counting
        """
        for attr in attributedict:
            if not callable(attr) and not attr.startswith("__"):
                attributedict[attr] = cls.call_counter(attributedict[attr])

        return type.__new__(cls, clsname, superclasses, attributedict)


class A(metaclass=FuncCallCounter):
    def foo(self):
        pass

    def bar(self):
        pass


if __name__ == "__main__":
    x = A()
    print(x.foo.calls, x.bar.calls)
    x.foo()
    print(x.foo.calls, x.bar.calls)