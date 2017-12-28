
from helpers import sieve, prime_factorizations, isPrimeMR

primes = sieve(10**8)
setprimes = set(primes)
pfs = prime_factorizations(10**6)


def get_divisors(pf):
	if len(pf) == 0:
		yield 1
		return
	(prime, power) = pf.popitem()
	for p in range(power + 1):
		for divisor in get_divisors(pf):
			yield prime**p * divisor 
	pf[prime] = power

def get_pf(n):
	if n < len(pfs):
		return pfs[n]
	else:
		if isPrimeMR(n):
			return {n : 1}
		ans = {}
		for p in primes:

			if n < len(pfs) or n in setprimes:
				break
			power = 0
			while n % p == 0:
				power += 1
				n /= p 

			if power > 0:
				ans[p] = power 

		if n in setprimes:
			ans[n] = 1
		elif n > 1:
			recursive_ans = {k : v for (k, v) in pfs[n].items()}
			for (prime, power) in ans.items():
				if prime in recursive_ans:
					recursive_ans[prime] += power
				else:
					recursive_ans[prime] = power

			return recursive_ans 

		return ans

total = 0
for (i, b) in enumerate(primes):
	if i % 10000 == 0:
		print i
	middle_pf = get_pf(b + 1)
	squared_pf = {k : 2 * v for (k, v) in middle_pf.items()}
	for divisor in get_divisors(squared_pf):
		if divisor < b + 1:
			a = divisor - 1
			c = (b + 1) * (b + 1) / (a + 1) - 1
			if a in setprimes and c in setprimes:
				# print a, b, c
				total += a + b + c 

print total

'''

100315739184392
[Finished in 2957.5s]
'''