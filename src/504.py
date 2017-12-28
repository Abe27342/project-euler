'''


PICK'S THEOREM!!!!!!!!



'''
from helpers import gcd, memoize


gcd = memoize(gcd)


def number_of_lattice_points(a, b, c, d):
	twice_area = (b + d) * (a + c)
	num_boundary = gcd(a, b) + gcd(b, c) + gcd(c, d) + gcd(d, a)
	interior_lattice_points = (twice_area - num_boundary) / 2 + 1
	return interior_lattice_points

m = 100
squares = {i**2 for i in range(2*m)}

total = 0
for a in range(1, m + 1):
	for b in range(1, m + 1):
		for c in range(1, m + 1):
			for d in range(1, m + 1):
				if number_of_lattice_points(a, b, c, d) in squares:
					total += 1

print total
'''

694687
runs in 220 seconds. could be optimized. too lazy.

'''
