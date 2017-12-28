'''

T(0) = 1
T(1) = 10
T(n) = 10 T(n-1) + T(n-2)

By inspection, gcd(T(a), T(b)) = T(n) where n = gcd(a + 1, b + 1) - 1.

I'm sure this can be proven by induction in a similar way to the fibonacci identity, but i'm not putting in that effort.

'''
from helpers import fast_power, recurrence_matrix, solve_recurrence, gcd, memoize, fast_power_iterative, mult
from math import log
from collections import defaultdict

L = 2000


@memoize
def T(n, modulus):
	return solve_recurrence([10, 1], [[10], [1]], n, modulus)

x0 = [[10], [1]]

def output_exponent_first_negative(a, b):
	'''
	returns the output exponent when trying to compute
	x^a - 1, x^b + 1
	where a < b.
	'''
	if a < b:
		n = b / a
		if b - n * a == 0:
			n -= 1
		# then the above reduces to gcd(x^a - 1, x^{b - a*n} + 1)
		return output_exponent_first_negative(a, b - a * n)
	elif a == b:
		return 0
	else:
		# then we're alternating adding and subtracting so the sign of n matters.
		n = a / b
		# Make sure we hit the base case for the positive one.
		if a - n * b == 0:
			n -= 1
		if n % 2 == 1:
			# then the above reduces to gcd(x^{a - n * b} + 1, x^b + 1)
			return output_exponent_two_positive(b, a - n * b)
		else:
			# then the above reduces to gcd(x^{a - n * b} - 1, x^b + 1)
			return output_exponent_first_negative(a - n * b, b)

def output_exponent_two_positive(a, b):
	'''
	returns the output exponent when trying to compute
	x^a + 1, x^b + 1.
	'''
	if a == b:
		return a

	if b > a:
		a,b = b,a

	n = a / b
	if a - n * b == 0:
		n -= 1 
	if n % 2 == 0:
		# then the above reduces to gcd(x^{a - nb} + 1, x^b + 1).
		return output_exponent_two_positive(b, a - n * b)
	else:
		# then the above reduces to gcd(x^{a - nb} - 1, x^b + 1).
		return output_exponent_first_negative(a - n * b, b)

odd_c_counts = defaultdict(lambda : 0)
even_c_counts = defaultdict(lambda : 0)
for a in range(1, L + 1):
	for b in range(1, L + 1):
		exponent_to_increment = output_exponent_two_positive(a, b)
		odd_c_counts[exponent_to_increment] += 1
		if exponent_to_increment == 0:
			even_c_counts['n_equals_0'] += 1
		else:
			even_c_counts[exponent_to_increment] += 1

print len(odd_c_counts), len(even_c_counts)

modulus = 987898789

# For c = 1, the total is 10 * number of values for a and b, which is 10 * L * L
total = L * L * 10
for c in range(L, 1, -1):
	print c
	if c % 2 == 0:

				
		matrix = recurrence_matrix([10, 1])
		total += even_c_counts['n_equals_0'] * T(0, modulus)
		total += even_c_counts[0] * T(1, modulus)
		for exponent in range(1, L + 1):
			matrix = fast_power_iterative(matrix, c, modulus)
			xn = mult(matrix, x0, modulus)

			count = even_c_counts[exponent]

			total += count * xn[-1][0]
			total %= modulus
		'''
		for (key, count) in even_c_counts.items():
			if key == 'n_equals_0':
				total += count * T(0, modulus)
			else:
				total += count * T(c**key, modulus)
			total %= modulus
		'''	
	else:
		matrix = recurrence_matrix([10, 1])
		total += odd_c_counts[0] * T(1, modulus)
		for exponent in range(1, L + 1):
			matrix = fast_power_iterative(matrix, c, modulus)
			xn = mult(matrix, x0, modulus)

			count = odd_c_counts[exponent]

			total += count * xn[-1][0]
			total %= modulus

		'''
		for (key, count) in odd_c_counts.items():
			total += count * T(c**key, modulus)
			total %= modulus
		'''

print total
'''

10 should be 247399089
20 should be 819411000
50 should be 118730695


970746056
[Finished in 751.0s]
'''
#print gcd(2000**1940 + 1, 2000**1980 + 1)
#print gcd(2000**1980 + 1, 2000**40 - 1)
#print gcd(2000**1940 + 1, 2000**40 - 1)
#print gcd(2000**20 + 1, 2000**40 - 1)

