from helpers import sieve
lim = 50000000

primes = sieve(int(lim**0.5)+1)
l = []

for p1 in primes:
    for p2 in primes:
        if(p1**2+p2**3 > lim):
            break
        for p3 in primes:
            if(p1**2+p2**3+p3**4 > lim):
                break
            l.append(p1**2+p2**3+p3**4)
l = list(set(l))
print(len(l))