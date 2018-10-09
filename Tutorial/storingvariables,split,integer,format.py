#ask the user to input 2 values and store them in variables num1 and num2

num1, num2 = input('Enter two numbers ').split() #split makes it so if you type two numbers with a space between, it will count as two numbers

#convert the strings into integers

num1 = int(num1)                                 #need to convert to string because miles currently equals "enter two numbers..."
num2 = int(num2)

#add the values and store into a varialbe called sum

sum = num1 + num2

#subtract the values and store in a variable called difference

difference = num1 - num2

#multiply the values and store in a variable called product

product = num1 * num2
#Divide the values and store in a variable called Quotient

quotient = num1 / num2
#Use modulus on the values to find the remainder

Remainder = num1 % num2

#print values like: num1 operator num2 equals solution

print(num1, '+', num2, '=', sum)
print("{} - {} = {}".format(num1,num2,difference))
print("{} x {} = {}".format(num1,num2,product))
print("{} / {} = {}".format(num1,num2,quotient))
print("{} % {} = {}".format(num1,num2,Remainder))
