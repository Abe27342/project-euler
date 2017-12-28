from helpers import sieve

modulus = 1000000009
N = 100000000

primes = sieve(N)

print 'finished sieving primes'

answer = 1
for prime in primes:
	
	power = 0
	i = 1
	while N >= pow(prime, i):
		power += N / pow(prime, i)
		i += 1

	answer *= 1 + pow(prime, 2 * power, modulus)
	answer %= modulus

print answer
