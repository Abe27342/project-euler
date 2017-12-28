from helpers import prime_factorizations, sieve
from operator import mul

from sys import setrecursionlimit

# bold call but you gotta do what you gotta do to not rewrite your shitty recursive solution into one using a stack :^)^)^)^)^)^)^)^)^)
setrecursionlimit(10**4)


N = 120000

prime_factorizations = prime_factorizations(N)
primes = sieve(N)

# print prime_factorizations

def rad(n):
	return reduce(mul, prime_factorizations[n].keys())

def abc_hit(a, b, c):
	rad_factors = set(prime_factorizations[c].keys())
	b_factors = set(prime_factorizations[b].keys())
	a_factors = set(prime_factorizations[a].keys())
	rad_factors = rad_factors.union(b_factors)
	rad_factors = rad_factors.union(a_factors)
	return reduce(mul, rad_factors) < c and a_factors.intersection(b_factors) == set()

def possible_nums(prime_candidates, max_num, min_index):
	if min_index >= len(prime_candidates) or max_num < prime_candidates[min_index]:
		yield 1
		return
	first_power = 1
	while first_power <= max_num:
		for c in possible_nums(prime_candidates, max_num / first_power, min_index + 1):
			yield c * first_power
		first_power *= prime_candidates[min_index]


def possible_nums_for_primeset(prime_candidates, max_num):
	# print prime_candidates, max_num
	for c in possible_nums(prime_candidates, max_num, 0):
		yield c
'''
sanity check with shitty run time

total2 = 0
for c in range(2, N):
	for a in range(1, c / 2):
		if abc_hit(a, c - a, c):
			total2 += 1
			print a, c - a, c
print total2
'''

total = 0
for c in range(2, N):
	c_primes = prime_factorizations[c]
	fudge_factor = c / rad(c)
	prime_candidates = []
	for p in primes:
		if p >= fudge_factor:
			break
		if p not in c_primes.keys():
			prime_candidates.append(p)

	# We assume a < b, and a + b == c so we only need to look up to c / 2.
	for a in possible_nums_for_primeset(prime_candidates, c / 2):
		# print a
		if abc_hit(a, c - a, c):
			total += c
			print a,c - a,c

print total

