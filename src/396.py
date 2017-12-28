'''



'''
from expr_helpers import Mult, Exp, Add, Subtract, Num
from helpers import crt

class WeakGoodsteinSimulator:

	def __init__(self, digit_list, current_base):
		self.digit_list = digit_list
		self.current_base = current_base 

	def is_finished(self):
		return len(self.digit_list) == 0

	def advance_one(self):
		self.current_base += 1
		self.subtract_one()
		# print self.digit_list

	def subtract_one(self):
		index = -1
		while self.digit_list[index] == 0:
			self.digit_list[index] = self.current_base - 1
			index -= 1
		self.digit_list[index] -= 1
		# remove leading zeros.
		while len(self.digit_list) > 0 and self.digit_list[0] == 0:
			self.digit_list.remove(0)

	def get_num_to_finish(self):
		num_moves = 0
		while not self.is_finished():
			self.advance_one()
			num_moves += 1
		return num_moves


# it takes i + 1 moves to finish [1, 0] if we're currently in base i.
# so to finish [n, 0] from base
print [(i, WeakGoodsteinSimulator([1, 0, 0], i).get_num_to_finish()) for i in range(2, 10)]


def a0(i):
	return i + 1

def a1(i):
	return 2 * i + 1

def a2(i):
	return pow(2, i + 1) * (i + 1) - 1

# This one cheats a bit. Makes use of the fact we only need to know the answer modulo 10^9.
def a3(i):
	def a2_expr(i):
		return Subtract(Mult(Add(i, Num(1)), Exp(Num(2), Add(i, Num(1)))), Num(1))
	cur_expr = a2_expr(Num(i))
	for j in range(i):
		cur_expr = a2_expr(cur_expr)
		# Cheap hack to get the recursion limit to  not overflow, since we memoize stuff this way on the way up :P
		cur_expr.compute_value(5**9)
	five_remainder = cur_expr.compute_value(5**9)
	two_remainder = -1
	return crt([(two_remainder, 2**9), (five_remainder, 5**9)])

'''
To get G(n), write n in binary, then apply ai successively to the digits of n that are ones.

For example, for n = 10, we have n = 1010_2, hence
G(10) = a3(a1(2)) - 2.

a_d(i) returns the base that the weak goodstein sequence will end on if the simulator is given the input [[1, 0, ... , 0], i]
(where there are d copies of the zero).

In general, a_d(i) = a_{d-1}^{i + 1}(i).

'''
total = 0
total += a0(2)
total += a1(2)
total += a1(a0(2))
total += a2(2)
total += a2(a0(2))
total += a2(a1(2))
total += a2(a1(a0(2)))
total += a3(2)
total += a3(a0(2))
total += a3(a1(2))
total += a3(a1(a0(2)))
total += a3(a2(2))
total += a3(a2(a0(2)))
total += a3(a2(a1(2)))
total += a3(a2(a1(a0(2))))


total -= 30 #since we returned the base, and the base starts at 2, so we need to subtract 2 * 15 in order to get the number of elements in all the sequences.
print total % 10**9
print a2(a1(2)), a2(a1(a0(2)))

