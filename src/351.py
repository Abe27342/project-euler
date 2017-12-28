from helpers import gcd

n = 1000


memo = {}
# returns the sum of the totient function from 1 to n using black magic fucking mobius inversion xD
def sum_totient(n):
	if n in memo:
		return memo[n]
	elif n == 1:
		return 2
	else:
		total = (n + 3) * n / 2
		d = 2
		while d < n + 1:
			multiplier = 1
			increment = 1
			while n / d == n / (d + multiplier):
				multiplier *= 2
			if multiplier % 2 == 0:
				multiplier /= 2

			total -= multiplier * sum_totient(n / d)
			d += multiplier
		memo[n] = total
		return memo[n]

def answer(n):
	return 6 * ((n + 1) * n / 2 - sum_totient(n) + 1)


def f(n):
	total = 0

	for a in range(1, n + 1):
		for b in range(1, n + 1 - a):
			if gcd(a, b) != 1:
				total += 1

	total += n - 1
	return total * 6


print [f(i) for i in range(1, 100)]
print [answer(i) for i in range(1, 100)]
print answer(10 ** 8)
'''
some bullshit about (n+1) * n / 2 - sum_{i = 1}^n phi(i) ?????

'''

print 6 * (15 - sum([1, 1, 2, 2, 4]))