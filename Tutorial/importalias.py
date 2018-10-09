from decimal import Decimal as D                #can import one command from an entire module under an alias "D"

sum = D(0)                                      #below is an example or rounding error in python mathematics
sum += D("0.1")
sum += D("0.1")
sum += D("0.1")
sum -= D("0.3")

print('sum = ', sum)
print('.1+.1+.1-.3= ', .1+.1+.1-.3)