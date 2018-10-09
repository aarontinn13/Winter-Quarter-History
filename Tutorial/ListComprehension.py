print('some examples of list comprehension\n')
list = [1,2,3,4,5]

print([x*2 for x in list])
print([x for x in list if x >= 3])
print([((float(9)/5)*x + 32) for x in list])

print('\n************************************************\n')

print('Pythagorean triples')
print([(x,y,z) for x in range(1,30) for y in range(x,30) for z in range(y,30) if x**2 + y**2 == z**2])

print('\n************************************************\n')

colours = [ "red", "green", "yellow", "blue" ]
things = [ "house", "car", "tree"  ]
print([ (x,y) for x in colours for y in things ])

print('\n************************************************\n')

noprimes = [j for i in range(2, 8) for j in range(i*2, 100, i)]
print([x for x in range(2, 100) if x not in noprimes])

from math import sqrt
n = 100
sqrt_n = int(sqrt(n))
no_primes = [j for i in range(2,sqrt_n) for j in range(i*2, n, i)]
print(no_primes)

print('\n************************************************\n')
'''
To create set, we change square bracket to curly bracket
'''
n = 100
sqrt_n = int(sqrt(n))
no_primes = {j for i in range(2,sqrt_n) for j in range(i*2, n, i)}
print(no_primes)

print('\n************************************************\n')

def primes(n):
    if n == 0:
        return []
    elif n == 1:
        return []
    else:
        p = primes(int(sqrt(n)))
        no_p = {j for i in p for j in range(i*2, n+1, i)}
        p = {x for x in range(2, n + 1) if x not in no_p}
    return p

for i in range(1,50):
    print(i, primes(i))