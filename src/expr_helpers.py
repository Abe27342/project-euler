from helpers import sieve, isPrimeMR, memoize

def euler_phi(n):
	primes = sieve(1000)

	answer = 1
	for prime in primes:
		if n == 1:
			break
		power = 0
		while n % prime == 0:
			power += 1
			n /= prime 
		if power > 0:
			answer *= (prime - 1) * prime**(power - 1)

	assert n == 1 or isPrimeMR(n)
	if n > 1:
		answer *= n - 1
	return answer


class Num:

	def __init__(self, const_val):
		self.val = const_val

	def compute_value(self, modulus):
		return self.val % modulus

class Add:
	def __init__(self, expr1, expr2):
		self.expr1 = expr1
		self.expr2 = expr2

	def compute_value(self, modulus):
		val1 = self.expr1.compute_value(modulus)
		val2 = self.expr2.compute_value(modulus)
		return (val1 + val2) % modulus



class Subtract:

	def __init__(self, expr1, expr2):
		self.expr1 = expr1
		self.expr2 = expr2
	@memoize
	def compute_value(self, modulus):
		val1 = self.expr1.compute_value(modulus)
		val2 = self.expr2.compute_value(modulus)
		return (val1 - val2) % modulus

class Mult:

	def __init__(self, expr1, expr2):
		self.expr1 = expr1
		self.expr2 = expr2

	@memoize
	def compute_value(self, modulus):
		val1 = self.expr1.compute_value(modulus)
		val2 = self.expr2.compute_value(modulus)
		return (val1 * val2) % modulus

class Exp:

	def __init__(self, base_expr, exponent_expr):
		self.base_expr = base_expr
		self.exponent_expr = exponent_expr
	@memoize
	def compute_value(self, modulus):
		exponent_val = self.exponent_expr.compute_value(euler_phi(modulus))
		base_val = self.base_expr.compute_value(modulus)
		return pow(base_val, exponent_val, modulus)
