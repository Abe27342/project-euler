'''

Compute the desired sum modulo the required stuff, then use CRT to combine.

'''

from helpers import gcd

def all_fibs(modulus):
	cur = 0
	last = 1
	while True:
		yield cur
		last,cur = cur, (last + cur) % modulus


def get_recurring_part(modulus):
	nums = []
	for num in all_fibs(modulus):
		nums.append(num)
		if len(nums) > 2 and (nums[-2], nums[-1]) == (0, 1):
			return nums[:-2]

def is_terminating_expression(x, modulus):
	return gcd(x, modulus) > 1



def compute_at_value(fib_sequence_recurring_part, x, modulus):
	total = 0
	if is_terminating_expression(x, modulus):
		pow_of_x = 1
		while (x**pow_of_x) % modulus != 0:
			total += fib_sequence_recurring_part[pow_of_x] * pow(x, pow_of_x, modulus)
			total %= modulus
			pow_of_x += 1
		return total
	else:
		# Need to do a little math to determine periodicity of solution
		fib_period = len(fib_sequence_recurring_part)
		pow_period = 1
		while pow(x, pow_period, modulus) != 1:
			pow_period += 1
		total_period = fib_period * pow_period / gcd(fib_period, pow_period)

		for pow_of_x in xrange(total_period):
			total += fib_sequence_recurring_part[pow_of_x % fib_period] * pow(x, pow_of_x, modulus)
			total %= modulus

		total *= 10**15 / total_period
		total %= modulus
		remaining_portion = 10**15 % total_period

		for pow_of_x in xrange(remaining_portion + 1):
			total += fib_sequence_recurring_part[pow_of_x % fib_period] * pow(x, pow_of_x, modulus)
			total %= modulus

		return total

def compute_polynomial_sum(modulus):
	fib_sequence_recurring_part = get_recurring_part(modulus)

	total = 0
	for x in range(1, 101):
		total += compute_at_value(fib_sequence_recurring_part, x, modulus)
	total %= modulus
	total = int(total)
	return total

required_moduli = [2**11, 3**6, 5**3, 7**2, 11, 13]
# print len(get_recurring_part(2**11))
# print len(get_recurring_part(3**6))
# print len(get_recurring_part(5**3))
# print len(get_recurring_part(7**2))
# print len(get_recurring_part(11))
# print len(get_recurring_part(13))

print [compute_polynomial_sum(modulus) for modulus in required_moduli]
print [i for i in required_moduli]

'''
Mathematica does the rest.

ChineseRemainder[{1334, 207, 50, 41, 0, 10},
 {2048, 729, 125, 49, 11, 13}]

 252541322550

 '''