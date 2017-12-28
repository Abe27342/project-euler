
from helpers import prime_factorizations, modinv, sieve
from collections import defaultdict

'''

659104042
[Finished in 177.4s]

However, it needs like 4 GB of ram to run that fast.
Turning down the number of pfs precomputed will reduce ram usage, but increase compute time.

'''


limit = 10**7
modulus = 1000000007

pfs = prime_factorizations((limit + 1) / 2)

n = limit

primes = sieve(limit + 1)
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



print 'got prime factorizations. wheew'


def compute_answer():
	total = 0
	current_coeff_pf = defaultdict(lambda : 0)
	current_coeff = 1

	current_r = 1

	for k in range(1, (n + 1) / 2 + 1):
		if k % 10000 == 0:
			print k, (n + 1) / 2

		current_coeff *= (n - k + 1)
		current_coeff *= modinv(k, modulus)
		current_coeff %= modulus
		
		required_mult_num = 1
		required_mult_den = 1
		for prime, power in get_pf(n - k + 1).items():
			old_power = current_coeff_pf[prime]
			current_coeff_pf[prime] += power
			new_power = old_power + power
			required_mult_num *= pow(prime, new_power, modulus) + 1
			required_mult_num %= modulus

			assert new_power >= 0
			if new_power < 0:
				print 'hi'
				print n - k + 1, get_pf(n - k + 1), new_power

			if old_power > 0:
				required_mult_den *= pow(prime, old_power, modulus) + 1
				required_mult_den %= modulus

		for prime, power in get_pf(k).items():
			# print k, get_pf(k)
			old_power = current_coeff_pf[prime]
			current_coeff_pf[prime] -= power
			new_power = old_power - power 
			if new_power < 0:
				print k, get_pf(k), old_power

			if new_power > 0:
				required_mult_num *= pow(prime, new_power, modulus) + 1
				required_mult_num %= modulus

			required_mult_den *= pow(prime, old_power, modulus) + 1
			required_mult_den %= modulus

			if current_coeff_pf[prime] == 0:
				del current_coeff_pf[prime]

		# print required_mult_num, required_mult_den, modinv(required_mult_den, modulus) * required_mult_den % modulus
		current_r *= required_mult_num * modinv(required_mult_den, modulus)
		current_r %= modulus

		total += 2 * (current_r - current_coeff)
		total %= modulus
		# print k, current_r - current_coeff, current_coeff #, total, current_coeff
		# print k

	total -= (current_r - current_coeff)
	total %= modulus

	return total

'''
real_pfs = prime_factorizations(limit + 1)

for i in range(2, limit + 1):
	if get_pf(i) != real_pfs[i]:
		print get_pf(i), real_pfs[i], i
'''


print compute_answer()
# print get_pf(50)
# print get_pf(51)
# print get_pf(52)
# print get_pf(56)

'''

for 10^6 should break
747100792


for 10^5 should be 
628701600
'''

