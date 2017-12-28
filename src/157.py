'''

Experimentation.

Intuitively, we have 10^n/a + 10^n / b = p, 
so 10^n / a and 10^n / b need to have the same denominator in their fully reduced form.

Call this denominator x and write a = dx, b = ex.

then d | 10^n and e | 10^n.

So we look at all numbers that are 10^n over something, then all pairwise sums of such numbers, then all factors of those pairwise sums to figure out the possibilities for d.

53490
[Finished in 43.8s]

'''
from helpers import prime_factorizations, isPrimeMR, sieve
from fractions import Fraction
from itertools import product


pfs = prime_factorizations(10**6)
primes = sieve(10**8)

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

def num_solutions(n):
	ten_to_the_n_divisors = [2**i * 5**j for i in range(n + 1) for j in range(n + 1)]
	solutions = set()
	for (d, e) in product(ten_to_the_n_divisors, ten_to_the_n_divisors):
		for x in get_divisors(get_pf(d + e)):
			
			a = (10**n / d) * x
			b = (10**n / e) * x
			p = Fraction(10**n, a) + Fraction(10**n, b)
			# print d, e, x, a, b, p
			assert p.denominator == 1
			p = p.numerator
			a, b = max(a, b), min(a, b)
			solutions.add((a, b, p))
			if len(solutions) > 10**6:
				return 'memory hard :('
	return len(solutions)

total = 0
for n in range(1, 10):
	print n
	total += num_solutions(n)
print total