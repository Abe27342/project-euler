from helpers import sieve, prime_factorizations
from random import random
from bisect import bisect_left

limit = 10**8

primes = sieve(limit)

cumsum = 0
cumulative_sums = []
for prime in primes:
	cumsum += prime 
	cumulative_sums.append(cumsum)


def highest_power_of_k_dividing_n_factorial(k, n):
	answer = 0
	k_power = 1
	while n / k**k_power > 0:
		answer += n / k**k_power
		k_power += 1
	return answer

def s(prime, power):
	if power <= prime:
		return power * prime
	else:
		guess = power * prime
		while highest_power_of_k_dividing_n_factorial(prime, guess) >= power:
			guess -= prime
		return guess + prime


def find_lt(a, x):
    'Find rightmost index less than x'
    i = bisect_left(a, x)
    if i:
        return i - 1
    raise ValueError

current_num_stack = []

num_computed = [0]
def S(call_stack_size, current_num, previous_max_value, prime_power_pair, minimum_index_for_next_prime):
	assert call_stack_size < 30
	assert current_num <= limit
	if prime_power_pair == tuple():
		max_value = 0
	else:

		assert current_num <= limit
		# print current_num
		num_computed[0] += 1
		prime, power = prime_power_pair
		max_value = max(s(prime, power), previous_max_value)

	total = max_value

	for next_index in range(minimum_index_for_next_prime, len(primes)):
		if current_num * primes[next_index] >= limit:
			break
		if random() < 0.001:
			print num_computed

		
		if current_num * primes[next_index]**2 > limit and max_value <= primes[next_index]:
			# In this case, only possible numbers we want to calculate left are given by current_num * some_big_prime
			# where the given prime is big enough to force the max value to be exactly that big prime.
			# So we move along to our precomputed lookup array, add the sum, and return it.
			#print current_num, previous_max_value, prime_power_pair, minimum_index_for_next_prime
			biggest_prime_index = find_lt(primes, limit / current_num)
			if biggest_prime_index + 1 < len(primes) and primes[biggest_prime_index + 1] == limit / current_num:
				biggest_prime_index += 1
			# print primes[biggest_prime_index], primes[next_index], current_num
			num_computed[0] += biggest_prime_index - next_index + 1
			total += cumulative_sums[biggest_prime_index] - cumulative_sums[next_index - 1]
			#print 'new total: %s' % total
			return total
		

		power = 1
		while current_num * primes[next_index]**power <= limit:
			total += S(call_stack_size + 1, current_num * primes[next_index]**power, max_value, (primes[next_index], power), next_index + 1)
			power += 1

	return total

print len(primes) + len(cumulative_sums)
print S(0, 1, 0, tuple(), 0)


# print wtf().S(9, 0, (3, 2), 2)
def general_s(l):
	return max([s(prime, power) for (prime, power) in l])


'''

Takes fucking YEARS to run. Ugh.

(like 20 hours)

'''