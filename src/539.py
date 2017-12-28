


from helpers import memoize


@memoize
def P(n):
	k = n / 4
	if n == 1:
		return 1
	elif n in [2, 3, 4]:
		return 2
	elif n % 4 in [0, 1]:
		return 4 * P(k) - 2
	else:
		return 4 * P(k)

@memoize
def S(n):
	return sum([P(i) for i in range(1, n + 1)])

@memoize
def fast_S(n):
	if n < 5:
		return S(n)
	if n % 4 != 3:
		return P(n) + fast_S(n - 1)
	else:
		k = n / 4
		return S(3) + 16 * fast_S(k) - 4 * k


n = 10**18

print fast_S(n) % 987654321


