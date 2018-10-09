#sets unlike lists or tuples can't have multiple occurrences of the same element.
#sets will only take one iterance of a value and will not take any additional copies.
x = set('abcdefg')
print(x)
x = set('aaaaaaa')
print(x)
x = set([1,2,3,4,5])
print(x)
x = {1,2,3,4,5}
print(x)
del x

#can add immutable values to a set
x = {1,2,3,4,5}
x.add('string')                        #we could not for example add a list to this set
print(x)

#clear a set
x.clear()
print(x)

#create a shallow copy
x = {1,2,3,4}
y = x.copy()
print(x)
print(y)
x.clear()
print(x)
print(y)
y.clear()

#find the differences between sets
x = {1,2,3,4,5}
y = {3,4,5,6,7}
z = {6,7,8,9,0}

print(x.difference(y))                      #return x excluding same values of y
print(y.difference(x))                      #return y excluding same values of x
print(x.difference(y).difference(z))        #return x excluding same values of y and z
x.clear()
y.clear()
z.clear()

#update difference x = x - y
x = {1,2,3,4,5}
y = {3,4,5,6,7}
z = {6,7,8,9,0}

x.difference_update(y)                      #return AND CHANGE x excluding same values of y
print(x)
y = y - z                                   #same as above
print(y)
x.clear()
y.clear()
z.clear()

#discard (if value is not present, do nothing)
x = {1,2,3,4,5}
y = {3,4,5,6,7}
z = {6,7,8,9,0}

x.discard(1)                              #remove 1 from the set
print(x)
#remove works like discard (if value is not present, return keyerror)
x.remove(2)
print(x)
x.clear()
y.clear()
z.clear()

#union to join sets omitting duplicates (temporary)
x = {1,2,3,4,5}
y = {3,4,5,6,7}

print(x.union(y))                          #Can use this
print(x|y)                                 #or this

#intersection to return similar values (temporary)
x = {1,2,3,4,5}
y = {3,4,5,6,7}

print(x.intersection(y))                   #Can use this)
print(x&y)                                 #or this
x.clear()
y.clear()

#isdisjoint returns true if sets have no similar values
x = {1,2,3,4,5}
y = {3,4,5,6,7}
z = {6,7,8,9,0}

print(x.isdisjoint(y))
print(x.isdisjoint(z))

#subset checks if set is subset or proper subset of another set
x = {1,2,3,4,5}
y = {3,4,5}

print(x<y)                                  #check if x is a proper subset of y
print(x>y)                                  #check if y is a proper subset of x
print(x.issubset(y))                        #can use this form
print(x<=y)                                 #or this form
print(y.issubset(x))
print(y<=x)

#superset checks if set is subset or proper subset of another set

print(x.issuperset(y))                      #can use this form
print(x>=y)                                 #or this form
print(x.issuperset(y))
print(y>=x)

#pop() removes and returns a random value within a set (returns value error if nothing in set
x = {1,2,3,4,5}
print(x.pop())
print(x.pop())
print(x.pop())
print(x.pop())
print(x.pop())


