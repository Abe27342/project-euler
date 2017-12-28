from helpers import sieve

N = 10 ** 7

def M(p, q, n):
	assert p < q
	x = p * q

	while x <= n:
		x *= p 
	x /= p 
	# now have p^a * q for largest possible value of a. Now we increase q and decrease p as necessary.
	current_best = x
	while x % p == 0 and x % q == 0:
		x *= q
		while x % p == 0 and x > n:
			x /= p
		if x % p == 0 and x > current_best:
			current_best = x

	return current_best

def S(n):
	primes = sieve(n)
	print 'primes done'
	total = 0
	for i in range(len(primes)):
		if primes[i] * primes[i + 1] > n:
			break
		print i
		p = primes[i]
		for j in range(i + 1, len(primes)):
			q = primes[j]
			if p * q > n:
				break
			total += M(p, q, n)

	return total


print S(N)