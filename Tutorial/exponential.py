import math

''' e is the max number that returns when you compound a 100% return over a certain period of time '''
''' e is the maximal rate of 'doubling' '''
print('e = {}'.format(math.e))

'''the higher the compound gets, the closer it gets to e'''
time = 3
rate = 100/100
number = 1
compound = 100000
print((number + (rate*number)/compound) ** (compound * time) )


'''natural log (ln) is the time needed to obtain a certain amount of growth at 100% continuous compounding'''

print(math.log1p(math.e))