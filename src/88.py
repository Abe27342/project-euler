import itertools
import functools
from operator import mul
from helpers import sieve
primes = sieve(24000)
#there's always a solution given for k by 2k = (k,2,1,1,1,1,...,1) so we only need to look in range(1,k+1)
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
'''
given the prime factor list, we need a way to return all sets that multiply to n.

Sets with size 1 = n

Sets with size 2 = 


'''

def get_n(k):
    done = False
    count = 2
    #while(not done):
        
    return()
        


