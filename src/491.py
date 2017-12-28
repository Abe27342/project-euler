'''
Key observation is that number is divisible by 11 iff its alternating digit sum is divisible by 11

so for a given set of digits in the odd positions, that set can be permuted however we like and same for the digits
in the even positions.

Doing so lets us limit ourselves to compute these constant values for only the 20 choose 10 possible sets, which is feasible.

'''
from itertools import combinations
from math import factorial
from helpers import memoize

@memoize
def fact(n):
	return factorial(n)

def number_of_ways_to_permute_list(L):
	counts = {l : L.count(l) for l in L}
	return factorial(len(L)) / reduce(lambda a, b: a * b, counts.values())


N = 10
digit_indices = [i for i in range(2 * N)]



total = 0
for positive_digit_indices in combinations(digit_indices, N):
	should_skip = False
	for index in positive_digit_indices:
		if index % 2 == 1 and index - 1 not in positive_digit_indices:
			should_skip = True 
	if should_skip:
		continue
	positive_digits = [positive_digit_index / 2 for positive_digit_index in positive_digit_indices]
	positive_digit_indices = set(positive_digit_indices)
	negative_digit_indices = [index for index in digit_indices if index not in positive_digit_indices]
	negative_digits = [index / 2 for index in negative_digit_indices]
	if (sum(positive_digits) - sum(negative_digits)) % 11 == 0:
		total += (N - positive_digits.count(0)) * number_of_ways_to_permute_list(negative_digits) * number_of_ways_to_permute_list(positive_digits) / N

print total
