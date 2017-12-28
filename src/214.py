from helpers import sieve, prime_factorizations
from collections import defaultdict

limit = 10**6 * 40

primes = sieve(limit)
setprimes = set(primes)

small_prime_factorizations = prime_factorizations(limit / 40)
small_totient_chain_length = [0]

def euler_phi(prime_factorization):
	answer = 1
	for (prime, power) in prime_factorization.items():
		answer *= prime - 1
		answer *= prime**(power - 1)
	return answer

def compute_chain_length(i):
	if i == 1:
		return 1
	prime_factorization = small_prime_factorizations[i]
	phi_i = euler_phi(prime_factorization)
	return 1 + small_totient_chain_length[phi_i]

def get_chain_length(n):
	if n < len(small_totient_chain_length):
		return small_totient_chain_length[n]
	else:
		prime_factorization = defaultdict(lambda : 0)
		for prime in primes:
			if prime > n or n in setprimes or n == 1:
				break

			while n % prime == 0:
				prime_factorization[prime] += 1
				n /= prime

		if n in setprimes:
			prime_factorization[n] += 1

		phi_n = 1
		for prime, power in prime_factorization.items():
			phi_n *= (prime - 1) * prime**(power - 1)
			
		return 1 + get_chain_length(phi_n)

for i in range(1, limit / 40):
	small_totient_chain_length.append(compute_chain_length(i))


# print [i for i in range(len(small_totient_chain_length)) if small_totient_chain_length[i] == 6 if i in setprimes]
# print len(primes)


print 'going through primes now'
total = 0
for prime in primes:
	if get_chain_length(prime) == 25:
		print prime
		total += prime

print total
