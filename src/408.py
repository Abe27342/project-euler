from math import sqrt
from helpers import memoize

N = 500
modulus = 10**9 + 7
squares = set([i**2 for i in range(1, int(sqrt(2 * N)) + 1)])


@memoize
def num_admissible_paths(x, y, modulus):
	if x == 0 or y == 0:
		return 1
	if x in squares and y in squares and x + y in squares:
		print x,y
		return 0
	return num_admissible_paths(x - 1, y, modulus) + num_admissible_paths(x, y - 1, modulus) % modulus


def P(n, modulus):
	return num_admissible_paths(n, n, modulus)


print P(N, modulus)