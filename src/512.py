from helpers import sum_totient, memoize, sieve_euler_phi
'''

Answer is phi(1) + phi(3) + ... + phi(n - 1) where it's n-1 since 5 * 10**8 is even.

'''


def slow_G(n):
	vals = sieve_euler_phi(n + 1)
	return sum(vals[1 : n + 1 : 2])


def G(n):
	if n % 2 == 0:
		return G(n - 1)
	else:
		if n == 1:
			return 1
		else:
			return sum_totient(n) - sum_even(n - 1)

def sum_even(n):
	assert n % 2 == 0
	if n == 0:
		return 1
	elif n == 2:
		return 2
	else:
		k = n / 2
		if k % 2 == 0:
			# -1 because phi(0) doesn't have a coefficient of 2 on it
			return sum_even(k) + sum_totient(k) - 1
		else:
			# -1 because phi(0) doesn't have a coefficient of 2 on it
			return sum_even(k - 1) + sum_totient(k) - 1

# N = 10**4

N = 5 * 10**8
# print slow_G(N)
print G(N)
# print sum_totient(4)