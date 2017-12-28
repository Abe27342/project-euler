

from helpers import sieve
from math import log, ceil

N = 10**6

primes = sieve(N)

partition_parts = [[0 for i in range(int(ceil(log(N, 3))))] for j in range(int(ceil(log(N, 2))))]

p2 = 0
while 2 ** p2 < N:

	p3 = 0
	while 2**p2 * 3**p3 < N:
		num = 2**p2 * 3**p3
		# print p2, p3, num
		partition_parts[p2][p3] = num

		p3 += 1
	p2 += 1

partition_parts = [[i for i in l if i != 0] for l in partition_parts]
flattened_partition_parts = [item for sublist in partition_parts for item in sublist]
print partition_parts

partition_counts_for_primes = {prime : 0 for prime in primes}

# max_second_index is exclusive, as in we've already seen a number which uses this index.
def consider_partitions(current_total_is_new, current_running_total, current_first_index, max_second_index):
	if current_running_total >= N:
		return
	if current_total_is_new and current_running_total in partition_counts_for_primes:
		partition_counts_for_primes[current_running_total] += 1

	if current_first_index >= len(partition_parts):
		return
	if max_second_index == 0:
		return
	# 'Lose it' case
	consider_partitions(False, current_running_total, current_first_index + 1, max_second_index)

	for partition_index in range(min(len(partition_parts[current_first_index]), max_second_index)):
		partition_part = partition_parts[current_first_index][partition_index]
		consider_partitions(True, current_running_total + partition_part, current_first_index + 1, partition_index)

consider_partitions(True, 0, 0, len(partition_parts[0]))

# print partition_counts_for_primes
print sum([prime for prime in primes if partition_counts_for_primes[prime] == 1])