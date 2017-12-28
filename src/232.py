
from helpers import memoize
from math import log

@memoize
def p(p1_total, p2_total):
	'''
	returns the probability of winning starting with player 2 playing first, where
	each of them have the desired totals.
	'''
	if p2_total >= 100:
		return 1.0
	if p1_total >= 100:
		return 0.0
	'''
	Otherwise, T should be picked to maximize probability of winning. If player 2 picks a value of T, then with probability
	1/2^T she'll have a value of p2_total + 2^{T - 1}.
	(Clearly T <= int(log(100 - p2_total, 2)))
	So:
	p(p1, p2) = 1/2^{T + 1} * (p(p1 + 1, p2 + 2^{T - 1}) + p(p1, p2 + 2^{T - 1})) + (1 - )
	'''
	max_prob = 0
	for T in range(1, int(log(100 - p2_total, 2)) + 3):
		candidate = pow(2, -T - 1) * (p(p1_total + 1, p2_total + pow(2, T - 1)) + p(p1_total, p2_total + pow(2, T - 1)))
		candidate += (0.5 - pow(2, -T - 1)) * (p(p1_total + 1, p2_total)) #+ p(p1_total, p2_total))
		# We want to write that last + sign, but it leads to an infinite recursive call. So we just solve the equation instead:
		candidate /= (0.5 + pow(2, -T - 1))
		if candidate > max_prob:
			max_prob = candidate
	return max_prob

print int(log(32, 2))

# print p(99, 90)
print (p(1, 0) + p(0, 0)) / 2