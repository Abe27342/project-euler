from helpers import sieve

primes = sieve(1000000)
prime_pow = [[p**power for power in range(1, 21) if p**power < 1000000] for p in primes]
print('primes generated')

phi_n = [0 for i in range(10000001)]


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
                
def get_digit_list(n):
    l = []
    for i in str(n):
        if(l.count([i,str(n).count(i)]) == 0):
            l.append([i,str(n).count(i)])
    l.sort()
    return(l)

sieve_phi(10000000)
print('phis calculated')
x = [[n,phi_n[n]] for n in range(2,10000001) if get_digit_list(n) == get_digit_list(phi_n[n])]
print('sorting')
x.sort(key=lambda x:x[0]/x[1])
print(x)