#If age is 5 go to Kindergarten
# ages 6 - 17 grades 1 - 12
# age > 17 go to college
# Try to complete program in 10 or less lines

age = eval(input('Enter Age '))
if(age == 5):
    print('Go to Kindergarten')
elif(age >= 6) and (age <= 17):
    grade = age - 5
    print('Go to grade {}'.format(grade))
elif(age > 17):
    print('Go to College')
else:
    print('Too young for school')
