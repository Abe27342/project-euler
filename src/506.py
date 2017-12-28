'''

Sequence repeats every 6 numbers.

1 2 3 4 3 2

total sum of the sequence is 15.


let f(i) be the position on which number i starts, when taken modulo 6.

'''
from helpers import modinv
from expr_helpers import Exp, Subtract, Mult, Num, Add

class Simulator:

	def __init__(self):
		self.current_position = 0
		self.digits = [1, 2, 3, 4, 3, 2]
		self.end_indices = {}
		self.largest_num_computed = 0

	def take_next_digit(self):
		self.number += self.digits[self.current_position % 6]
		self.current_position += 1

	def compute_num_start(self, target):
		self.number = 0
		while self.number < target:
			self.take_next_digit()
		assert self.number == target
		self.end_indices[target] = self.current_position

	def get_index_of_end(self, n):
		if n in self.end_indices:
			return self.end_indices[n]

		for target_num in range(self.largest_num_computed + 1, n + 1):
			self.compute_num_start(target_num)
		self.largest_num_computed = n 
		return self.end_indices[n]

	def get_index_of_start(self, n):
		if n == 1:
			return 1
		return self.get_index_of_end(n - 1) + 1

	def get_num(self, n):
		start_index = self.get_index_of_start(n) - 1
		end_index = self.get_index_of_end(n) - 1
		if end_index / 6 == start_index / 6:
			return int(''.join([str(i) for i in self.digits[start_index % 6 : end_index % 6 + 1]]))
		else:
			first_part = ''.join([str(i) for i in self.digits[start_index % 6 :]])
			middle_part = ''.join((end_index / 6 - start_index / 6 - 1) * [str(i) for i in self.digits])
			end_part = ''.join([str(i) for i in self.digits[:end_index % 6 + 1]])
			return int(first_part + middle_part + end_part)

def S(n):
	s = Simulator()
	return sum([s.get_num(i) for i in range(1, n + 1)])

modulus = 123454321

s = Simulator()

def get_a(k_mod_15):
	start_index, end_index = (s.get_index_of_start(k_mod_15) % 6, s.get_index_of_end(k_mod_15) % 6) 
	first_num = s.get_num(k_mod_15)
	second_num = s.get_num(k_mod_15 + 15)
	ratio = 10**6
	a = second_num - first_num
	return a

def fifteen_cycle_sum(n):
	s = Simulator()
	cycle_of_15_sum = sum([s.get_num(i) for i in range(1, 16)])
	num_full_cycles = n / 15
	partial_cycle = n % 15
	partial_cycle_sum = sum([s.get_num(i) for i in range(1, partial_cycle + 1)])
	return (num_full_cycles * cycle_of_15_sum + partial_cycle_sum)

def fast_S(n):
	# Every number after the first 15 will just be some number of copies of 123432 and then the digits given in the cycle of 15 sum.
	# So split this number into the 123432 parts and the cycle of 15 parts.
	total = fifteen_cycle_sum(n)
	
	# Now we have to account for the copies of 123432.
	num_full_cycles = n / 15
	
	num_full_cycles_expr = Num(num_full_cycles)
		
	partial_cycle = n % 15
		
	if num_full_cycles > 0 and partial_cycle != 0:
		# For each number in multipliers, this adds a 123432(1 + 10^6 + 10^12 + ... + 10^(6 * num_full_cycles)) amount.
		# this sums to 123432 * modinv(10^6 - 1) * (10^(6 * num_full_cycles - 6) - 1).
		large_power_expr = Exp(Num(10), Mult(Num(6), num_full_cycles_expr))
		# print 'doing partial cycle stuff'
		for i in range(1, partial_cycle + 1):
			# print get_a(i) + 10**6 * get_a(i)
			total +=  get_a(i) * modinv(10**6 - 1, modulus) * (large_power_expr.compute_value(modulus) - 1) % modulus
		
	if num_full_cycles > 1:

		''' Mathematica blesses me by summing the shitty geometric series.'''
		r = 10**6

		total += sum([get_a(k) for k in range(1, 16)]) * modinv((r - 1)**2, modulus) * (Exp(Num(10**6), num_full_cycles_expr).compute_value(modulus) - 1 - (r - 1) * num_full_cycles)

	return total % modulus

# It appears the cycle is 15 long.
# Not surprising since the sum of 1 + 2 + 3 + 4 + 3 + 2 is 15.
print [(s.get_index_of_start(i) % 6, s.get_index_of_end(i) % 6)  for i in range(1, 16)]
print [s.get_num(i) for i in range(5, 100, 15)]



# print S(15) % modulus
print fast_S(15)
# [get_a(i) for i in range(1, 16)]

i = 15
# print S(i), fast_S(i)
print fast_S(10**14)
