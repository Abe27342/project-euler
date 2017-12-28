'''

Observation says it's the coefficient on x^d on sum_{i = 0}^{m-1} (n choose i) (x-1)^i

Mathematica tells me this is (up to absolute value) equal to (m-d) / (n-d) * (m choose d) * (n choose d)

'''
from helpers import modinv

modulus = 999999937

n = 10**13
m = 10**12
d = 10**4

answer = m - d
answer *= modinv(n - d, modulus)

def binom(n, k, modulus):
	result = 1
	for i in range(n, n - k, -1):
		result *= i 
		result %= modulus

	for i in range(1, k + 1):
		result *= modinv(i, modulus)
		result %= modulus
	return result

answer *= binom(m, d, modulus) * binom(n % modulus, m % modulus, modulus) * binom(n / modulus, m / modulus, modulus)
answer %= modulus

'''
Use lucas theorem to do last binomial.
10^13 in base modulus is, from last digit to first, 630000, 10000
10^12 in base modulus is, from last digit to first, 63000, 1000
'''
print 10**12 / modulus
expected_answer =  227197811615775 % modulus

print answer, expected_answer