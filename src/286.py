'''

Attempt to use normal distribution.

Mean of normal distribution is 50 - 50*51/(2q)

variance of normal distribution is 425 * (-101 + 3q)/q^2


this fails.

Instead, let f(i, j, q) be the probability that the first i RV's yield j hits.

then f(i, j) = (1 - i / q) * f(i - 1, j - 1, q) + i/q * f(i - 1, j, q).

'''
from helpers import memoize

@memoize
def f(i, j, q):
	if j > i or j < 0:
		return 0
	if i == 1:
		if j == 0:
			return 1.0 / q
		else:
			assert j == 1
			return 1 - 1.0 / q
	else:
		total = 0
		total += (1 - float(i) / q) * f(i - 1, j - 1, q)
		total += float(i) / q * f(i - 1, j, q)
		return total


print f(50, 20, 52.64945719531)