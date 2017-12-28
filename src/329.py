from fractions import Fraction
from helpers import sieve



primes = set(sieve(500))

memo = {}

def left_hop(n):
	if n > 1:
		return n - 1
	assert n == 1
	return 2

def right_hop(n):
	if n < 500:
		return n + 1
	assert n == 500
	return 499

def probability(n, string):
	if (n,string) in memo:
		return memo[(n, string)]
	elif len(string) == 1:
		if n in primes and string == 'P':
			memo[(n,string)] = Fraction(2, 3)
			return Fraction(2, 3)
		if n in primes and string == 'N':
			memo[(n,string)] = Fraction(1, 3)
			return Fraction(1, 3)
		if n not in primes and string == 'P':
			memo[(n,string)] = Fraction(1, 3)
			return Fraction(1, 3)
		if n not in primes and string == 'N':
			memo[(n,string)] = Fraction(2, 3)
			return Fraction(2, 3)

	memo[(n, string)] = probability(n, string[0]) * Fraction(1, 2) * (probability(left_hop(n), string[1:]) + probability(right_hop(n), string[1:]))
	return memo[(n, string)]

def total_probability(string):
	answer = 0
	for n in range(1, 501):
		answer += probability(n, string) * Fraction(1, 500)
	return answer

print total_probability('PPPPNNPPPNPPNPN')
