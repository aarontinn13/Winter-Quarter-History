from copy import deepcopy

list1 = [1,2,3,4,5]             #creating list1
list2 = [6,7,8,9,10]            #creating list2
list1.append(list2)             #attaching list2 into list 1
print(list1)                    #can see list1 has list2 in index[5]

list3 = list1                   #This function will not create a copy but rather a 'link', there is no new object, just rename.
list3 = list1.copy()            #in order to shallow copy you can either slice copy [n1:n2] or x.copy()
list3[2] = 'x'                  #shallow copy will create separate objects for one layer...
print(list1)                    #as you can see list1 was unchanged
print(list3)                    #and list3 has changed

list3[5][0] = 'y'               #shallow copy however does not let you change deeper layers within a list of a list
print(list1)                    #as you can see list1 was changed
print(list3)                    #as is list3

list3 = deepcopy(list1)         #in order to create two entirely different objects we must deepcopy
                                #lets try and change something in list1
                                #and list2
list1[5][3] = 'This is change 1'
list3[5][1] = 'This is change 2'
print(list1)
print(list3)                    #as you can see we are successful!!!!


