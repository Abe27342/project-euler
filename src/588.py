from helpers import memoize

def get_coeff(p, i):
	''' returns the coefficient on x^i in the array p. '''
	if i >= len(p) or i < 0:
		return 0
	return p[i]


@memoize
def get_ones_list(n):
	ones_list = [1]
	for i in range(n):
		next_ones_list = [0] * (4 + len(ones_list))
		for j in range(len(next_ones_list)):
			next_ones_list[j] = (get_coeff(ones_list, j) + get_coeff(ones_list, j - 1) + get_coeff(ones_list, j - 2) + get_coeff(ones_list, j - 3) + get_coeff(ones_list, j - 4)) % 2
		ones_list = next_ones_list
	return ones_list

@memoize
def get_zero_gaps(n):
	ones_list = get_ones_list(n)
	zero_gap_lengths = [len(gap) for gap in ''.join([str(i) for i in ones_list]).split('1')]
	return zero_gap_lengths

@memoize
def slow_q(k):
	return sum(get_ones_list(k))

def fast_q(k):
	bin_k = bin(k)[2:]
	components = bin_k.split('00')
	ans = 1
	for component in components:
		if len(component) > 0:
			n = int(component, 2)
			if n > 0:
				print 'calling slow_q on %s' % n
				ans *= slow_q(n)
	return ans

print sum([fast_q(10**i) for i in range(1, 19)])


'''
print [slow_q(i) for i in range(50)]

k = 2**6 + 1

# print [slow_q(k) * 5 - slow_q(2**8 + k) for k in range(2**6, 2**6 + 20)]

print slow_q(2**8 + k), slow_q(k) * 5

print slow_q(2**6 + 4)

print get_zero_gaps(2**6 + 2)

print get_zero_gaps(2**8 + k)
print get_zero_gaps(k)

for 10 it's
[0, 1, 1, 1, 3, 1, 1, 3, 1, 1, 3, 1, 1, 3, 1, 1, 1, 0]

for 100 it's 
[0, 3, 3, 3, 3, 15, 3, 3, 3, 3, 79, 3, 3, 3, 3, 47, 3, 3, 3, 3, 47, 3, 3, 3, 3, 79, 3, 3, 3, 3, 15, 3, 3, 3, 3, 0]

for 1000 it's
[0, 7, 7, 7, 15, 7, 7, 7, 95, 7, 7, 7, 15, 7, 7, 7, 95, 7, 7, 7, 15, 7, 7, 7, 95, 7, 7, 7, 15, 7, 7, 7, 95, 7, 7, 7, 15, 7, 7, 7, 95, 7, 7, 7, 15, 7, 7, 7, 95, 7, 7, 7, 15, 7, 7, 15, 7, 7, 15, 7, 7, 7, 31, 7, 7, 7, 15, 7, 7, 15, 7, 7, 15, 7, 7, 7, 31, 7, 7, 7, 15, 7, 7, 15, 7, 7, 15, 7, 7, 7, 31, 7, 7, 7, 15, 7, 7, 15, 7, 7, 15, 7, 7, 7, 31, 7, 7, 7, 15, 7, 7, 15, 7, 7, 15, 7, 7, 7, 31, 7, 7, 7, 15, 7, 7, 15, 7, 7, 15, 7, 7, 7, 31, 7, 7, 7, 15, 7, 7, 15, 7, 7, 15, 7, 7, 15, 7, 7, 7, 31, 7, 7, 7, 15, 7, 7, 15, 7, 7, 15, 7, 7, 7, 31, 7, 7, 7, 15, 7, 7, 15, 7, 7, 15, 7, 7, 7, 31, 7, 7, 7, 15, 7, 7, 15, 7, 7, 15, 7, 7, 7, 31, 7, 7, 7, 15, 7, 7, 15, 7, 7, 15, 7, 7, 7, 31, 7, 7, 7, 15, 7, 7, 15, 7, 7, 15, 7, 7, 7, 31, 7, 7, 7, 15, 7, 7, 15, 7, 7, 15, 7, 7, 7, 95, 7, 7, 7, 15, 7, 7, 7, 95, 7, 7, 7, 15, 7, 7, 7, 95, 7, 7, 7, 15, 7, 7, 7, 95, 7, 7, 7, 15, 7, 7, 7, 95, 7, 7, 7, 15, 7, 7, 7, 95, 7, 7, 7, 15, 7, 7, 7, 0]


it appears gaps in 2^k are
[0, 2^k - 1, 2^k - 1, 2^k - 1, 2^k - 1, 0]

so for nonadjacent things we're in pretty good shape.


turns out this extends whenever there's a gap of 2 zeros in the binary expansion, so we just parse and use slow_q.
done.

'''
