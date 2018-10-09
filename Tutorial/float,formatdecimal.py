your_float = input("Enter a float: ")

your_float = float(your_float)

print("Rounded to 2 decimals: {:.2f}".format(your_float))
#use :.xf to round to x decimal places

#have the user enter their investment amount and expected interest
#Each year their investment will increase by their investment + their investment * interest
investment_amount = float(input('Please enter your investment amount: '))
expected_interest = float(input('Please enter your expected yearly interest: ')) * .01
years = eval(input('Please enter years of investment: '))

for x in range(years): #this range will calculate from 0 - years
    investment_amount = investment_amount + (investment_amount*expected_interest)
print("Investment after {} year(s): {:.2f}".format(years, investment_amount))

#floats are not exactly, exact. They go up to 16 digits, after that they become bogus.
