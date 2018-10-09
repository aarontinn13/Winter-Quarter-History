#enter calculation: 5*6

#5*6 = 30

#store the user input of 2 numbers and the operator
num1, operator, num2 = input('Enter Calculation ').split()

#convert the strings into integers

num1 = float(num1)
num2 = float(num2)

#if + then we need to provide output based on addition

if operator == "+":
    print("{} + {} = {}".format(num1, num2, num1 + num2))
elif operator == "-":
    print('{} - {} = {}'.format(num1, num2, num1 - num2))
elif operator == "*":
    print('{} * {} = {}'.format(num1, num2, num1 * num2))
elif operator == "/":
    print('{} / {} = {}'.format(num1, num2, num1 / num2))
else:
    print("Please use the operators + - * / only")

#print the result