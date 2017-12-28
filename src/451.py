from helpers import prime_factorizations, crt, sieve
from itertools import product
'''
153651073760956
[Finished in 2605.0s]

'''


limit = 2 * 10**7
# N = 2 * 10 ** 7

pfs = prime_factorizations(limit / 20)
primes = sieve(limit)
setprimes = set(primes)

def get_pf(n):
	if n < len(pfs):
		return pfs[n]
	else:
		if n in setprimes:
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

def l(n):
	pf = get_pf(n)
	max_candidate = 0
	
	if 2 not in pf or pf[2] == 1:
		for a_options in product([-1, 1], repeat = len(pf)):
			pf_separate = [prime**power for (prime, power) in pf.items()]
			crt_list = [(a_options[i], pf_separate[i]) for i in range(len(pf))]
			candidate = crt(crt_list)
			if candidate < n - 1 and candidate > max_candidate:
				max_candidate = candidate 
	else:
		pf_without_2 = {k : v for (k, v) in pf.items() if k != 2}
		two_pow = pf[2]
		for two_options in [-1, 1, 2**(two_pow - 1) - 1, 2**(two_pow - 1) + 1]:
			for a_options in product([-1, 1], repeat = len(pf_without_2)):
				pf_separate = [prime**power for (prime, power) in pf_without_2.items()]
				crt_list = [(a_options[i], pf_separate[i]) for i in range(len(pf_without_2))]
				crt_list.append((two_options, 2**two_pow))
				candidate = crt(crt_list)
				if candidate < n - 1 and candidate > max_candidate:
					max_candidate = candidate 
	return max_candidate

total = 0 
for n in range(3, limit + 1):
	if n % 10000 == 0:
		print n, limit
	total += l(n)

print total
