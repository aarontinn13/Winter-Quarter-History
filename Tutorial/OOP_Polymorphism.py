'''
Polymorphism is construed from two Greek words. "Poly" stands for "much" or "many" and
"morph" means shape or form. Polymorphism is the state or condition of being polymorphous,
or if we use the translations of the components "the ability to be in many shapes or forms.
Polymorphism is a term used in many scientific areas. In Crystallography it defines the
state, if something crystallizes into two or more chemically identical but crystallographically
distinct forms. Biologists know polymorphism as the existence of an organism in several form
or colour varieties. The Romans even had a god, called Morpheus, who is able to take any human
form: Morheus appears in Ovid's metamorphoses and is the son of Somnus, the god of sleep.
You can admire Morpheus and Iris in the picture on the right side.

So, before we fall to sleep, we get back to Python and to what polymorphism means in the
programming language context. Polymorphism in Computer Science is the ability to present the
same interface for differing underlying forms. We can have in some programming languages
polymorphic functions or methods for example. Polymorphic functions or methods can be applied
to arguments of different types, and they can behave differently depending on the type of the
arguments to which they are applied. We can also define the same function name with a varying
number of parameter.

Let's have a look at the following Python function:
'''

def f(x, y):
    print("values: ", x, y)

f(42, 43)
f(42, 43.7)
f(42.3, 43)
f(42.0, 43.9)

'''


We can call this function with various types, as demonstrated in the example. In typed 
programming languages like Java or C++, we would have to overload f to implement the various 
type combinations. 

Python is implicitly polymorphic. We can apply our previously defined function f even to 
lists, strings or other types, which can be printed: 
'''

f([3,5,6],(3,5))
f("A String", ("A tuple", "with Strings"))
f({2,3,9}, {"a":3.4,"b":7.8, "c":9.04})
