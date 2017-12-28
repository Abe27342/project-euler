'''

Observation: for a given fraction, the number of steps before reducing is the number of steps before we hit the next smallest factor.

We always reduce to 1 / another number

and so we always eliminate all of the smallest factors.

So f(n) = largest_prime_factor(n + 1) - 1.

'''

from helpers import prime_factorizations, isPrimeMR, sieve

limit = 2 * 10**6


primes = sieve(limit + 100)
pfs = prime_factorizations(limit + 100)

def get_pf(n):
	if n < len(pfs):
		return pfs[n]
	else:
		if isPrimeMR(n):
			return {n : 1}
		ans = {}
		for p in primes:

			if n < len(pfs) or isPrimeMR(n):
				break
			power = 0
			while n % p == 0:
				power += 1
				n /= p 

			if power > 0:
				ans[p] = power 

		if isPrimeMR(n):
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

def largest_prime_factor(n):
	if n == 1:
		return 0
	pf = get_pf(n)
	return max(pf.keys())

total = 0
for k in range(1, limit + 1):
	if k % 10000 == 0:
		print k
	total += max(largest_prime_factor(k + 1), largest_prime_factor(k**2 - k + 1)) - 1

print total