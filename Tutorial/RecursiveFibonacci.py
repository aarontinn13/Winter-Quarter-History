# 1,1,2,3,5,8,13,21,34,55,89
# 1,2,3,4,5,6, 7, 8, 9,10,11

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
print(fib(40))

print()

def fib_iteration(n):
    old, new = 0, 1
    if n == 0:
        return 0
    for i in range(n-1):
        old, new = new, old + new
    return new
print(fib_iteration(8))

print()
print('**********************************EXERCISES**********************************')
print('**********************************PROBLEM 1**********************************')
#Think of a recusive version of the function f(n) = 3 * n, i.e. the multiples of 3
def mult3(n):
    if n == 1:
        return 3
    else:
        return mult3(n-1) + 3
for i in range(1,10):
    print(mult3(i))
print()
print('**********************************PROBLEM 2**********************************')
#Write a recursive Python function that returns the sum of the first n integers.
def problem2(n):
    if n == 1:
        return 1
    else:
        return n + problem2(n-1)

print(problem2(5))

print()
print('**********************************PROBLEM 3**********************************')
#Write a function which implements the Pascal's triangle:
def pascal(n):
    if n == 1:
        return [1]
    else:
        line = [1]
        previous_line = pascal(n-1)
        for i in range(len(previous_line)-1):
            line.append(previous_line[i] + previous_line[i+1])
        line += [1]
    return line

print(pascal(3))

#OR

def pascal1(n):
    if n == 1:
        return [1]
    else:
        p_line = pascal1(n-1)
        line = [ p_line[i]+p_line[i+1] for i in range(len(p_line)-1)]
        line.insert(0,1)
        line.append(1)
    return line

print(pascal1(3))

print()
print('**********************************PROBLEM 4**********************************')
#The Fibonacci numbers are hidden inside of Pascal's triangle.
#If you sum up the coloured numbers of the following triangle, you will get the 7th Fibonacci number:
def fib_pascal(n,fib_pos):
    if n == 1:
        line = [1]
        fib_sum = 1 if fib_pos == 0 else 0
    else:
        line = [1]
        (previous_line, fib_sum) = fib_pascal(n-1, fib_pos+1)
        for i in range(len(previous_line)-1):
            line.append(previous_line[i] + previous_line[i+1])
        line += [1]
        if fib_pos < len(line):
            fib_sum += line[fib_pos]
    return (line, fib_sum)

def fib(n):
    return fib_pascal(n,0)[1]

# and now printing out the first ten Fibonacci numbers:
for i in range(1,10):
    print(fib(i))

print()
print('**********************************PROBLEM 5**********************************')
#Implement a recursive function in Python for the sieve of Eratosthenes.
#The sieve of Eratosthenes is a simple algorithm for finding all prime numbers up to a specified integer. It was created by the ancient Greek mathematician Eratosthenes.
#2,3,5,7,11,13,17,19,23,29
def isprime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True

def getprime(max):
    listofprimes = []
    for num1 in range(2, max):
        if isprime(num1):
            listofprimes.append(num1)
    return listofprimes

max = int(input('What is the max Prime? '))         #6
listofprimes = getprime(max)
for prime in listofprimes:
    print(prime)

