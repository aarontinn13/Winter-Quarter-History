#how to create a dictionary
aaronDict = {"fname": "Aaron", "lname": "Tinn", "address":"123 main Street"}

#printing a definition of a specific key
print(aaronDict['fname'])

#how to replace a definition in dictionary
aaronDict['address'] = '456 main Street'

#how to print a dictionary (dictionaries natively sort by definition first)
print(aaronDict)

#how to add a key and definition to an existing dictionary
aaronDict['city'] = 'Dublin'

#how to check if there is a key within an existing dictionary, will print true or false
print('city' in aaronDict)

#how to print the values in the dictionary only
print(aaronDict.values())
'''
or 
for key in aaronDict:
    print(aaronDict[key])
'''

#how to print the keys in the dictionary only
print(aaronDict.keys())
'''
or
for key in aaronDict:
    print(key)
'''

#how to loop through a dictionary (and print both keys and definitions)
for k, v in aaronDict.items():
    print(k,v)

#how to retrieve a specific definition in a dictionary and how to 'else' if it doesn't exist
print(aaronDict.get('mName', 'Not Here')) #'mName is not a key in the dictionary, returns 'Not Here'
print(aaronDict.get('lname', 'Not Here')) #lname i
'''
this is similar to 
aaronDict.pop('mName', 'Not Here')
but pop will remove and retrieve simultaneously
'''

#how to delete keys and definition
del aaronDict['fname']

#how to clear the entire dictionary
aaronDict.clear()
print(aaronDict)

#how to concatenate dictionaries, note that definition will overwrite similar key in updated dictionary!
dict1 = {'Bill':'1', 'John':'2', 'Chad':'3'}
dict2 = {'Chris': '4', 'Fred':'5', 'John': '6'}

dict1.update(dict2)
print(dict1)
print(dict2)

#how to change dictionary to a list
itemsofdict1 = dict1.items()        #making a tuple of the dictionary
print(itemsofdict1)
items = list(itemsofdict1)
print(items)
keysofdict1 = dict1.keys()          #making a list of the keys of the dictionary
print(keysofdict1)
keys = list(keysofdict1)
print(keys)
valuesofdict1 = dict1.values()      #making a list of the values of the dictionary
print(valuesofdict1)
values = list(valuesofdict1)
print(values)

#how to change a list into a dictionary
print(dict(zip(keys,values)))

#how to add keys and definitions to a list
employees = []
fName, lName = input('Enter Employee Name: ').split()
employees.append({'fName': fName, 'lName' : lName})
print(employees)

#how to create an array dictionary

customers = []

while True:

    createEntry = str(input('Enter Customer (Yes/No): '))
    createEntry = createEntry.lower()

    if createEntry == 'no':
        break
    elif createEntry == 'yes':
        fName, lName = input('Enter Customer Name Please: ').split()
        customers.append({'fName': fName, 'lName': lName})
    else:
        print(('Please enter either "Yes" or "No"'))

for cust in customers:
    print(cust['fName'], cust['lName'])