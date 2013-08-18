from helpers import sieve
import functools
from operator import mul
import copy

primes = sieve(1000000)
prime_set_list = [[] for i in range(1000001)]
calculated_chain = [False for i in range(1000001)]
f = []


def proper_divisor_sum(n):
    p_set = prime_set_list[n]
    if(n == 0):
        return(0)
    if(n == 1):
        return(1)
    return(functools.reduce(mul, [int((p_set[i][0]**(p_set[i][1]+1)-1)/(p_set[i][0]-1)) for i in range(len(p_set))])- n)

def print_list():
    for i in range(101):
        print(prime_set_list[i],i)


def recursive_prime_set(n, largestPrimeInN, isNewPrime, lim):
    if(n > lim):
        return
    
    if(isNewPrime):
        prime_set_list[n] = copy.deepcopy(prime_set_list[round(n/largestPrimeInN)])
        prime_set_list[n].append([largestPrimeInN,1])
        
        for p in primes:
            if(p*n > lim):
                break
            if(p < largestPrimeInN):
                continue
            elif(p == largestPrimeInN):
                recursive_prime_set(p*n,p,False,lim)
            else:
                recursive_prime_set(p*n,p,True,lim)
    else:
        
        prime_set_list[n] = copy.deepcopy(prime_set_list[round(n/largestPrimeInN)])
        prime_set_list[n][-1][1] += 1
        
        for p in primes:
            if(p*n > lim):
                break
            if(p < largestPrimeInN):
                continue
            elif(p == largestPrimeInN):
                recursive_prime_set(p*n,p,False,lim)
            else:
                recursive_prime_set(p*n,p,True,lim)
        
def sieve_prime_set(n):
    lim = n
    for p in primes:
        prime_set_list[p] = [[p,1]]
    #print_list()
    for p in primes:
        for p2 in primes:
            if(p*p2 > lim):
                break
            if(p2 < p):
                continue
            elif(p2 == p):
                recursive_prime_set(p2*p,p,False,lim)
            else:
                recursive_prime_set(p*p2,p2,True,lim)




def calculate_chain(x,f):
    l = [x]
    while(x < 1000000 and calculated_chain[x] == False):
        calculated_chain[x] = True
        x = f[x]
        l.append(x)
    if(l.count(l[-1]) == 1):
        return([0])
    else:
        return(l[l.index(l[-1]):-1])

max_length_of_chain = 0
chain_with_max_length = []

l = 1000000
sieve_prime_set(l)
f = [proper_divisor_sum(i) for i in range(l+1)]

print(f[12496],f[f[12496]],f[f[f[12496]]],f[f[f[f[12496]]]])

print('done')
#print_list()

maximum = 0
maximum_list = []
i = 2
while(i < 1000001):
    if(not calculated_chain[i]):
        potential = calculate_chain(i,f)
        if(len(potential) > maximum):
            maximum = len(potential)
            maximum_list = potential
    i += 1
print('actually done')
print(maximum)
maximum_list.sort()
print(maximum_list[0])



    