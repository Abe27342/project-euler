from helpers import sieve
from functools import reduce
from operator import mul
primes = sieve(1000000)
print('primes generated')

product = 1
count = 0
while product < 1000000:
    product *= primes[count]
    count += 1
count -= 1
product /= primes[count]
print(product)
'''

Ignore all of this code. I'm rather dumb.
def prime_factors(n):
    if(n == 1):
        return([])
    if(n in primes):
        return([[n,1]])
    for p in primes:
        if(p < int(n**0.5)+1):
            if(n % p == 0):
                power = 1
                while(n % (p**power) == 0):
                    power += 1
                power -= 1
                x = prime_factors(int(n/(p**power)))
                x.append([p,power])
                return(x)
def phi(n):
    if(n == 0):
        return(1)
    if(n == 1):
        return(1)
    p_set = prime_factors(n)
    return(n*reduce(mul,[1-1/p_set[i][0] for i in range(len(p_set))]))

print('making set')
x = [n/phi(n) for n in range(1000)]
print('made set, finding max')
maximum = max(x)
print([n for n in range(1000) if x[n] == maximum])
'''