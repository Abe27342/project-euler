from helpers import memoize

@memoize
def f(n):
	if n == 1 or n == 3:
		return n
	elif n % 2 == 0:
		return f(n / 2)
	elif n % 4 == 1:
		return 2 * f(2 * (n / 4) + 1) - f(n / 4)
	else:
		return 3 * f(2 * (n / 4) + 1) - 2 * f(n / 4)

@memoize
def odd_sum(n):
	# verify input is an odd number.
	if n % 2 == 0:
		n -= 1
	if n == 1:
		return 1
	if n == 3:
		return 4

	if n % 4 == 3:
		k = n / 4
		return 5 * odd_sum(2 * k + 1) - 3 * S(k) - 1

	assert n % 4 == 1
	k = n / 4
	return odd_sum(4 * k + 3) - f(4 * k + 3)

@memoize
def S(n):
	if n == 1:
		return 1
	if n == 3:
		return 5
	return S(n / 2) + odd_sum(n)


#print odd_sum(100)
#print S(8)
#print S(4)
#print odd_sum(7) # should be 16.
# odd_sum(7) = 5 * odd_sum(3) - 3 * S(1)
#            = 5 * 4 - 3
# f(15) + f(13) + f(11) + f(9) + f(7) + f(5) + f(3) + f(1) = 5f(7) - 3f(3) + 5f(5) - 3f(2) + 5f(3) - 3f(1) + f(3) + f(1)
#          = 5 * (odd_sum(7) - f(1)) - 3 * S(3) + 3 + 1
#print 6 * f(3) - 2 * f(1)
#print odd_sum(5)

n = 100
print S(3 ** 37) % 10 ** 9
