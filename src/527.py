from math import log
from helpers import memoize

@memoize
def binary_expected(n):
	if n == 1:
		return 1.0
	elif n == 2:
		return 1.5
	elif n % 2 == 1:
		k = n / 2
		return 1.0 / n + float(n - 1) / n * (1 + binary_expected(k))
	else:
		k = n / 2
		return 1.0 / n + (1 + binary_expected(k)) / 2 + float(k - 1) / n * (1 + binary_expected(k - 1))

@memoize
def random_expected(n):
	if n == 1:
		return 1.0
	elif n == 2:
		return 1.5
	else:
		total = 0
		for i in range(1, n):
			total += 2 * i * random_expected(i)
		total = float(total) / (n * n)
		total += 1.0
		return total

def H(n):
	total = 0
	for i in range(1, n + 1):
		total += 1.0 / i
	return total

def fast_random_expected(n):
	return -3 + 2 * float(1.0 / n + 1) * H(n)

def approx_H(n):
	return 0.5772156649 + log(n) + 1.0 / (2 * n) - 1.0 / (12 * n * n)

def approx_random_expected(n):
	return -3 + 2 * float(1.0 / n + 1) * approx_H(n)


print approx_random_expected(10**10) - binary_expected(10**10)
