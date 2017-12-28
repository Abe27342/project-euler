from fractions import Fraction
from helpers import memoize

class Num:

	def __init__(self, const_val):
		self.val = const_val

	def compute_value(self):
		return self.val

class Add:
	def __init__(self, expr1, expr2):
		self.expr1 = expr1
		self.expr2 = expr2

	def compute_value(self, modulus):
		val1 = self.expr1.compute_value()
		val2 = self.expr2.compute_value()
		return (val1 + val2)

class Subtract:

	def __init__(self, expr1, expr2):
		self.expr1 = expr1
		self.expr2 = expr2
	@memoize
	def compute_value(self):
		val1 = self.expr1.compute_value()
		val2 = self.expr2.compute_value()
		return (val1 - val2)

class Mult:

	def __init__(self, expr1, expr2):
		self.expr1 = expr1
		self.expr2 = expr2

	@memoize
	def compute_value(self):
		val1 = self.expr1.compute_value()
		val2 = self.expr2.compute_value()
		return (val1 * val2)


class Div:

	def __init__(self, expr1, expr2):
		self.expr1 = expr1
		self.expr2 = expr2

	@memoize
	def compute_value(self):
		val1 = self.expr1.compute_value()
		val2 = self.expr2.compute_value()
		return fraction(val1, val2)

# Doesn't work: can't get the thing in the example with this format.
@memoize
def reachable_nums(low_num, high_num):
	if low_num == high_num:
		return set([low_num])

	num_with_entire_range = int(''.join([str(i) for i in range(low_num, high_num + 1)]))	
	nums = set([num_with_entire_range])
	for next_low_num in range(low_num + 1, high_num + 1):
		
		for reachable_num2 in reachable_nums(next_low_num, high_num):
			for reachable_num1 in reachable_nums(low_num, next_low_num - 1):
				nums.add(reachable_num1 + reachable_num2)
				nums.add(reachable_num1 - reachable_num2)
				nums.add(reachable_num1 * reachable_num2)
				if reachable_num2 != 0:
					nums.add(Fraction(reachable_num1, reachable_num2))
	return nums

# print len(reachable_nums(1, 7))
print sum([i for i in reachable_nums(1, 9) if int(i) == i and i > 0])