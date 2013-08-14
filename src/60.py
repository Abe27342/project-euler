'''
idea: hope to god that the set is 3,7,109,673, p for some prime p.
'''
from helpers import sieve, isPrime
primes = sieve(100000)
print "primes generated"


not_done = True
def concat(a,b):
    return(int(str(a) + str(b)))
def check_concat(n):
    return(all([isPrime(concat(3,n)), isPrime(concat(n,3)), isPrime(concat(7,n)), isPrime(concat(n,7)), isPrime(concat(109,n)), isPrime(concat(n,109)), isPrime(concat(673,n)), isPrime(concat(n,673))]))
    

for p in primes:
    if check_concat(p):
        print(p)
print "none :("