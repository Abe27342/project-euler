from helpers import sieve
from itertools import combinations
from fractions import Fraction

primes = sieve(25)

n = reduce(lambda a, b : a * b, primes)
phin = reduce(lambda a,b : a * b, [i - 1 for i in primes])
'''
Just have to get i as small as possible where the first printed value is less than the second.

Answer is the third.

'''
i = 4
print float(i * phin) / (i * n - 1)
print float(15499) / 94744


print i * n
for (p1, p2) in combinations(primes, 2):
	potential_n = n * p1
	phi_potential_n = p2 * phin * p1 / (p1 - 1)
	if float(phi_potential_n) / (potential_n - 1) < float(15499) / 94744:
		print 'wtf'


