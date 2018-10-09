# We'll provide different outputs based on age
# age 1 - 18-> important
# 21, 50, > 65 ->
# All others -> Not Important

#receive age and store in age
age = eval(input('Enter age: '))
#eval() allows us to automatically evaluate data to assume its type
#and : If both are true it returns true
#or : If either condition is true then return true
#not : Convert a true condition into a false

#If age is both greater than or equal to 1 and less than or equal to 18 we want to print important message
if (age >= 1) and (age <= 18):
    print('Important Birthday')

#If age is either 21 or 50 or greater than 65, important
elif (age == 21) or (age == 50):
    print('Important Birthday')

#We want to check if age is less than 65, also convert true to false

elif not(age < 65):
    print('Important Birthday')

#Not Important
else:
    print('Sorry not important')