'''

First, a simulation.

'''

from helpers import memoize, modinv



class BowlSet:

	def __init__(self, n):
		self.bowls = [1 for i in range(n)]
		self.index = 0

	def make_move(self):
		num_beans = self.bowls[self.index]
		self.bowls[self.index] = 0
		while num_beans > 0:
			self.index += 1
			self.index %= len(self.bowls)
			self.bowls[self.index] += 1
			num_beans -= 1

	def num_to_repeat(self):
		num_moves = 1
		# print self.bowls
		self.make_move()
		while not self.is_finished():
			# print self.bowls
			num_moves += 1
			self.make_move()
		print 'done in %s moves' % num_moves
		return num_moves


	def is_finished(self):
		for i in self.bowls:
			if i != 1:
				return False
		return True

def binom(n, k):
	return fact(n) / (fact(k) * fact(n - k))

def finite_diffs(L):
	return [L[i + 1] - L[i] for i in range(len(L) - 1)]


# No idea why this formula works. Wolframalpha is good at pattern matching, though :)
def fast_M_of_two_to_k_plus_one(k):
	return 4**k + 2**(k + 1) - 3**k


modulus = 7**9
# can reduce exponent modulo phi(7^9) = 6 * 7^8
def fast_sum_of_M(n):
	reduced_n = n % (6 * 7**8)
	return (modinv(3, modulus) * (pow(4, reduced_n + 1, modulus) - 1) + 2 * (pow(2, reduced_n + 1, modulus) - 1) - modinv(2, modulus) * (pow(3, reduced_n + 1, modulus) - 1)) % modulus

print fast_sum_of_M(10**18)



nums = [BowlSet(2**i + 1).num_to_repeat() for i in range(10)]
print nums
nums2 = [4**i + 2**(i + 1) - 3**i for i in range(10)]
print nums2

'''

According to wolframalpha, we have closed form as
2^{2n} + 2^{n + 1} - 3^n 
(wtf?)

but it works!

'''