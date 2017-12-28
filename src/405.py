

# Assumes n is a multiple of 2, or 17, which is the case for moduluses we care about in this problem.
def euler_phi(n):
	answer = 1
	for prime in [2, 17]:
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


def f(n):
	return 2 * (2**n - 3 - (-1)**n)/3

print [f(i) for i in range(5)]

def T(n):
	if n in [0, 1]:
		return 0
	else:
		return 4 * T(n - 1) + (2**(n + 2) - (-1)**n) / 3 - 3

def explicit_T(n):
	return 1 + float(2 * 4**n) / 5 - float((-1)**n)/15 - float(2**(n+2)) / 3

# The random fucking numbers are inverses of 5, 15, and 3 respectively modulo 17^7.
def T_expr(n):
	term1 = Mult(Mult(Num(2), Exp(Num(4), n)), Num(246203204))
	term2 = Mult(Exp(Num(-1), n), Num(355626850))
	term3 = Mult(Exp(Num(2), Add(n, Num(2))), Num(136779558))
	first_two = Add(Num(1), term1)
	first_three = Subtract(first_two, term2)
	all_terms = Subtract(first_three, term3)
	return all_terms




'''4 * T(n-1) + f(n)  + (2**(n + 1) + (-1)**(n))/3 - 1'''

'''4 * (2**(n - 1) / 3)'''
print [(i, T(i)) for i in range(10)]
# print [(i, explicit_T(i)) for i in range(10)]

print T_expr(Exp(Num(10), Exp(Num(10), Num(18)))).compute_value(17**7)