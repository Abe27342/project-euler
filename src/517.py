'''
Idea: for each prime, need to find all distinct pairs of positive integers a,b where

n - sqrt(n) - 1 < a + b * sqrt(n) < n - sqrt(n).

Once we have this, answer is sum of (a + b choose b).


'''
from helpers import isPrimeMR, modinv
from math import sqrt, ceil

modulus = 1000000007

primes = []

low_limit = 10**7
high_limit = 10**7 + 10**4

for candidate in range(low_limit, high_limit):
	if isPrimeMR(candidate):
		primes.append(candidate)

print 'primes found, there are %s of them ' % len(primes)

k_facts = [1] + [0] * (high_limit - 1)
cumprod = 1
for k in range(1, high_limit):
	cumprod *= k
	cumprod %= modulus
	k_facts[k] = cumprod

k_facts_invs = [modinv(k, modulus) for k in k_facts]


def binom(n, k, modulus):
	if n < 0 or k < 0 or k > n:
		return 0

	if k > n - k:
		return binom(n, n - k, modulus)

	return (k_facts[n] * k_facts_invs[k] * k_facts_invs[n - k]) % modulus


def G(n, modulus):
	n_sq = sqrt(n)
	b = 0
	a = int(n - (b + 1) * n_sq)
	answer = 0
	while a >= 0:
		# Take care of 'forced exits', where both options put us above the n - sqrt(n) total distance traversed.
		answer += 2 * binom(a + b, b, modulus)
		
		# Now think about 'early exits', where we could have chosen to step 1 but instead we step sqrt(n).
		# In this case, for this b we have a minimum a value of ceil(n - (b + 2) * n_sq).
		min_a_val = max(0, ceil(n - (b + 2) * n_sq))
		min_a_val = int(min_a_val)
		max_a_val = a 
		
		'''
		# Now, we want to write this:
		for a in range(min_a_val, max_a_val): # exclusive since we took care of it by multiplying by 2 above.
			answer += binom(a + b, b, modulus)

		# but this would involve looping over 10**4 things for the actual problem size. So we collapse the sum into subtracting two binomial coefficients
		# using normal combinatorial identities (hockey stick).
		'''
		answer += binom(max_a_val + b, b + 1, modulus) - binom(min_a_val + b, b + 1, modulus)
		answer %= modulus

		b += 1
		a = int(n - (b + 1) * n_sq)


	return answer

print G(90, modulus)
print 7564511 % modulus

total = 0
for (i, prime) in enumerate(primes):
	print i, prime
	total += G(prime, modulus)
print total % modulus

'''
Uncommenting the above code gives
581468882

'''

