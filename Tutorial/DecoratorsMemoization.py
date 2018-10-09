def memoize(f):                                     #f = fib
    memo = {}
    def helper(x):                                  #x = 40
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
fib = memoize(fib)

print(fib(40))                                      #memoize(fib)(40)

print()
print('*********************************************************************************************')
print()


class Memoize:
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}
    def __call__(self, *args):
        if args not in self.memo:
	        self.memo[args] = self.fn(*args)
        return self.memo[args]

@Memoize
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
