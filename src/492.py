'''

Wolframalpha quickly shows that if r = (3 + sqrt(13)) / 2, then 

a(n) = 1/6 * (r^{2^n} + r^{-2^n} - 5).

From this, one can derive a separate recurrence b(n) for which:

b(n) = 3b(n-1) + b(n-2)
b(0) = 2
b(1) = 3

and it can be shown that a(n) = 1/6 * (b(2^n) - 5).


So

[[b_{n+1}], [b_n]] = [[3, 1], [1, 0]]^n * [[b_1], [b_0]].

For our purposes, though, the exponent value of n is extremely large, on the order of 2^10^15. So fast exponentiation is not enough.

To remedy this, we can reduce the exponent modulo |GL_2(Z/pZ)| = (p^2 - 1)(p^2 - p) since we only need to compute the result modulo p.

rest is very standard.

'''
from helpers import memoize, fast_power_iterative, mult, crt, isPrimeMR

@memoize
def b(n):
	if n == 1:
		return 3
	elif n == 0:
		return 2
	else:
		return 3 * b(n - 1) + b(n - 2)

def a(n):
	return (b(2**n) - 5) / 6

# returns a(n) taken modulo p.
def fast_a(n, p):
	A = [[3, 1], [1, 0]]
	exponent_reducing_modulus = (p * p - 1) * (p * p - p)
	reduced_exponent = pow(2, n, exponent_reducing_modulus)
	six_times_answer = mult(fast_power_iterative(A, reduced_exponent, p), [[3], [2]], p)[1][-1] - 5
	answer = crt([(six_times_answer, p), (0, 6)]) / 6
	return answer

def B(x, y, n):
	total = 0
	for p in range(x, x + y + 1):
		if p % 100000 == 0:
			print p
		if isPrimeMR(p):
			total += fast_a(n, p)

	return total

print B(10**9, 10**7, 10**15)