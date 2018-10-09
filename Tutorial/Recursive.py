def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))

#to see how it works we will debug with print functions
def factorial2(n):
    print("factorial2 has been called with n = " + str(n))
    if n == 1:
        return 1
    else:
        res = n * factorial2(n-1)
        print("intermediate result for ", n, " * factorial2(" ,n-1, "): ",res)
        return res

print(factorial2(5))
print()

def iterative_factorial(n):
    result = 1
    for i in range(2,n+1):
        result *= i
    return result

print(iterative_factorial(5))







