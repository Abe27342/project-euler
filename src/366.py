'''

By running the slow (comparative to the limit) simulation below, it becomes evident that the losing positions for the first player are
precisely the fibonacci numbers.

Interesting.

'''

from helpers import memoize
from itertools import product


@memoize
def win_or_lose(m, n):
	if m <= 0:
		return 'Lose'
	for i in range(1, n + 1):
		if win_or_lose(m - i, 2 * i) == 'Lose':
			return 'Win'

	return 'Lose'

def M(n):
	if win_or_lose(n, n - 1) == 'Lose':
		return 0
	else:
		for i in range(n - 1, 0, -1):
			if win_or_lose(n - i, 2 * i) == 'Lose':
				return i

# print [(i, i - 1) for i in range(1, 200) if win_or_lose(i, i - 1) == 'Lose']
# print [(i, M(i)) for i in range(1, 200)]


def get_fibs(limit):
	fs = [0, 1]
	while fs[-1] < limit:
		fs.append(fs[-1] + fs[-2])
	return fs 

fibs = get_fibs(10**18)

'''
returns the sum of M(n) from n = F_{2n} to n = F_{2n + 2}.
'''
def sum_of_M_over_fib_interval(n):
	highest_num = (fibs[2 * n + 1] - 1) / 2
	middle_num = (fibs[2 * n] - 1) / 2
	low_num = (fibs[2 * n - 1] - 1) / 2
	return (highest_num * (highest_num + 1) + middle_num * (middle_num + 1) + low_num * (low_num + 1)) / 2

def slow_sum_M(n):
	return sum([M(i) for i in range(1, n + 1)])

# returns the sum of M over the interval from F[2n] to F[2n + 1]
def sum_of_M_over_short_fib_interval(n):
	first_run_max = (fibs[2 * n] - 1) / 2
	total = first_run_max * (first_run_max + 1) / 2
	num_runs = n - 1
	for run_num in range(num_runs - 1):
		run_low_limit = 1 + (fibs[2 * run_num + 3] - 1) / 2
		run_high_limit = (fibs[2 * run_num + 4] - 1) / 2
		total += (-run_low_limit * (run_low_limit - 1) + run_high_limit * (run_high_limit + 1)) / 2
	return total

def sum_M(n):
	k = 2
	total = 0
	while 2 * k + 2 < len(fibs) and fibs[2 * k + 2] <= n:
		total += sum_of_M_over_fib_interval(k)
		k += 1

	currently_summed_to_index = 2 * k
	if fibs[2 * k + 1] <= n:
		total += sum_of_M_over_short_fib_interval(k)
		currently_summed_to_index = 2 * k + 1

	# Now we have fibs[currently_summed_to] < n < fibs[currently_summed_to + 1] and we need to sum M(i) for the remaining portion.
	number_of_numbers_left = n - fibs[currently_summed_to_index]

	next_range_max = (fibs[currently_summed_to_index] - 1) / 2
	if next_range_max > number_of_numbers_left:
		total += (number_of_numbers_left * (number_of_numbers_left + 1)) / 2
		return (total, 0)
	return (total, number_of_numbers_left)


# print fibs[-2]
print sum_M(10**18)[0] % 10**8

