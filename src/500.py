from heapq import heappush, heappop
from helpers import sieve

primes = sieve(10**7)
limit = 500500
modulus = 500500507

# want to throw in tuples onto the heap (factor_to_multiply, prime, power)
heap = [(prime, prime, 0) for prime in primes]

cur_num = 1
while limit > 0:
	factor_to_multiply, prime, power = heappop(heap)
	
	cur_num *= factor_to_multiply
	cur_num %= modulus
	heappush(heap, (factor_to_multiply * pow(prime, power + 1), prime, 2 * power + 1))

	limit -= 1

print cur_num