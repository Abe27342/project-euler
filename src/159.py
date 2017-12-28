from helpers import sieve
from collections import deque

N = 10 ** 6 - 1 

# ... and this is a misread too. It should really be "digital_root".
def digit_sum(n):
	while n >= 10:
		n = sum([int(i) for i in str(n)])
	return n
#lol.... "primes".
#Turns out my initial interpretation was wrong, but could be fixed by doing this :^)
primes = [i for i in range(2, N + 1)]#sieve(N)
primes_digit_sums = [digit_sum(prime) for prime in primes]


# mdrs[i] contains mdrs(i)
mdrs = [0] * (N + 1)

num = 1
factor_indices = deque([0])
can_append = True

while len(factor_indices) > 0:
	num = reduce(lambda accum, i: accum * primes[i], factor_indices, 1)
	if num > N:
		factor_indices.pop()
		can_append = False
	else:
		ds = sum([primes_digit_sums[i] for i in factor_indices])
		if ds > mdrs[num]:
			mdrs[num] = ds
		if can_append:
			i = factor_indices[-1]
			factor_indices.append(i)
		else:
			i = factor_indices.pop()
			if i + 1 < len(primes):
				factor_indices.append(i + 1)
			can_append = True



print mdrs[24]
print sum(mdrs)
