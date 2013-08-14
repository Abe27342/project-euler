from helpers import sieve
from functools import reduce
from operator import mul
primes = sieve(1000000)
prime_pow = [[p**power for power in range(1, 21) if p**power < 1000000] for p in primes]
print('primes generated')
phi_n = [0 for i in range(1000001)]
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
    if(phi_n[n] != 0):
        return(phi_n[n])
    if(n == 0):
        return(0)
    if(n == 1):
        return(0)
    if(n in primes):
        return(n-1)
    else:
        for p in primes:
            if(n % (p**2) == 0):
                return(phi_n[int(n/p)] * p)
            elif(n % p == 0):
                return(phi_n[int(n/p)] * (p-1))
def smallest_prime_factor(n):
    if(n in primes):
        return(n)
    for p in primes:
        if(n % p == 0):
          return(p)

def recursive_phi(n, largestPrimeInN, isNewPrime, lim):
    if(n > lim):
        return
    if(isNewPrime):
        phi_n[n] = phi_n[round(n/largestPrimeInN)]*(largestPrimeInN - 1)
        for p in primes:
            if(p*n > lim):
                break
            if(p < largestPrimeInN):
                continue
            elif(p == largestPrimeInN):
                recursive_phi(p*n,p,False,lim)
            else:
                recursive_phi(p*n,p,True,lim)
    else:
        phi_n[n] = phi_n[round(n/largestPrimeInN)]*largestPrimeInN
        for p in primes:
            if(p*n > lim):
                break
            if(p < largestPrimeInN):
                continue
            elif(p == largestPrimeInN):
                recursive_phi(p*n,p,False,lim)
            else:
                recursive_phi(p*n,p,True,lim)
        
def sieve_phi(n):
    lim = n
    for p in primes:
        phi_n[p] = p-1
        for p2 in primes:
            if(p*p2 > lim):
                break
            if(p2 < p):
                continue
            elif(p2 == p):
                recursive_phi(p2*p,p,False,lim)
            else:
                recursive_phi(p*p2,p2,True,lim)
'''
def sieve_phi(n):
    for p in primes:
        phi_n[p] = p-1
    print('phi_n initialized')
    lim = 500000
    for n,elem in enumerate(phi_n):
        if(n == 0 or n ==1):
            break
        print(n)
        if n > lim:
            break
        smallest_factor = smallest_prime_factor(n)
        for p in primes:
            if(p >= smallest_factor):
                power = 1
                #set the value of n * (p**power)
                while(n * (p**power) < 1000000):
                    phi_n[n*(p**power)]=elem*(p**power)
                    power += 1
'''
        #so what we want to do is take all primes and take p^k * n
sieve_phi(1000000)

#x = [phi(n) for n in range(2,101)]
#y = [sum([x[i] for i in range(n)]) for n in range(98)]
#print(x)
print(sum(phi_n))
#print(y)

