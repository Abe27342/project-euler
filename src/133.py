from helpers import sieve
primes = sieve(100)
print([i for i in primes if (i-1)%2 == 0 or (i-1) % 5== 0])


'''
(10^6 - 1) / 9


R(10^n) = (10^(10^n) - 1)/9

so we must have 10^(10^n) = 1 mod 9p has no solutions

sooo that means
phi(9p) = 6(p-1)
10^(10^n mod 6(p-1)) = 1 mod 9p has no solutions
'''