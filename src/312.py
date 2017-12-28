'''

After a little bit of math working out the recurrences below, we get that

C(n) = 2^{3^{n-2}} * 3^{(3^{n-2} - 3) / 2}

C(C(C(10000))) is incredibly shitty to write out, so it's probably easier to write an expression computer.

'''
from helpers import gcd
# Assumes n is a multiple of 2, 3, or 13, which is the case for moduluses we care about in this problem.
def euler_phi(n):
	answer = 1
	for prime in [2, 3, 13]:
		power = 0
		while n % prime == 0:
			n /= prime
			power += 1
		if power > 0:
			answer *= prime**(power - 1) * (prime - 1)
		
	return int(answer)

class Num:

	def __init__(self, const_val):
		self.val = const_val

	def compute_value(self, modulus):
		return self.val % modulus

class Subtraction:

	def __init__(self, expr1, expr2):
		self.expr1 = expr1
		self.expr2 = expr2

	def compute_value(self, modulus):
		val1 = self.expr1.compute_value(modulus)
		val2 = self.expr2.compute_value(modulus)
		return (val1 - val2) % modulus

class Mult:

	def __init__(self, expr1, expr2):
		self.expr1 = expr1
		self.expr2 = expr2

	def compute_value(self, modulus):
		val1 = self.expr1.compute_value(modulus)
		val2 = self.expr2.compute_value(modulus)
		return (val1 * val2) % modulus

class Exp:

	def __init__(self, base_expr, exponent_expr):
		self.base_expr = base_expr
		self.exponent_expr = exponent_expr

	def compute_value(self, modulus):
		exponent_val = self.exponent_expr.compute_value(euler_phi(modulus))
		base_val = self.base_expr.compute_value(modulus)
		return pow(base_val, exponent_val, modulus)

class MinusThreeOverTwo:
	# This is pretty sketchy, but it should work. Don't reuse this code unless you understand how special-purpose it is. :P
	def __init__(self, orig_expr):
		self.orig_expr = orig_expr

	def compute_value(self, modulus):
		orig_val = self.orig_expr.compute_value(modulus * 2)
		return ((orig_val - 3) / 2) % modulus


'''
from helpers import memoize

@memoize
def A(n, modulus):
	if n == 1:
		return 1
	if n == 2:
		return 3
	else:
		return (2 * B(n-1, modulus) * A(n-1, modulus)**2) % modulus

@memoize
def B(n, modulus):
	if n == 1:
		return 1
	if n == 2:
		return 2
	else:
		return (2 * B(n-1, modulus)**2 * A(n-1, modulus)) % modulus

@memoize
def C(n, modulus):
	return B(n-1, modulus)**3 % modulus
'''

#print [(A(i, 10**8), B(i, 10**8)) for i in range(1, 5)]
#x = [C(i, 10**8) for i in range(2, 10000)]
#print C(10000, 10**8)

def C(expr):
	two_power = Exp(Num(3), Subtraction(expr, Num(2)))
	three_power = MinusThreeOverTwo(two_power)
	return Mult(Exp(Num(2), two_power), Exp(Num(3), three_power))



answer = C(C(C(Num(10000))))
print answer.compute_value(13**8)
# answer = C(Num(10000))
# print answer.compute_value(13**8)


# print euler_phi(13 ** 8)
# print 12 * 13**7