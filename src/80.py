from decimal import *
import math
getcontext().prec = 120


def f(x):
    n = list(str(Decimal(x).sqrt()))

    n.remove('.')
    #print(n)
    #print(len(n))
    return(sum([int(n[i]) for i in range(100)]))

print(f(5))
#2 through 101 is 100 numbers, but 9 are square, so we gotta add up to 109
m = [f(x) for x in range(2,100) if x**0.5 != int(x**0.5)]
print(sum(m),len(m))