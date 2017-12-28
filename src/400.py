from helpers import memoize

'''
Uses 4 gigs of ram, and god is it ugly (to get the memory usage that low even. The idea is very nice, actually.)

438505383468410633
[Finished in 394.6s]

'''

@memoize
def nimber(k):
	'''
	returns the nimber of the kth fibonacci tree.
	'''
	if k < 3:
		return k - 1
	else:
		return (nimber(k - 1) + 1) ^ (nimber(k - 2) + 1)

# This is just to get the nimbers in the cache.
nimbers = [nimber(i) for i in range(1, 10001)]


modulus = 10**18


memo = {}
def number_of_ways_to_make(k, desired_nimber):
	'''
	returns the number of ways to make the kth fibonacci tree have the desired nimber by chopping off one node.
	'''
	if desired_nimber > max_reachable_nimbers[k]:
		return (True, 0)
	if (k, desired_nimber) in memo:
		return (True, memo[(k, desired_nimber)])
	if k == 1:
		memo[(k, desired_nimber)] = 0
		return (True, 0)
	elif k == 2:
		# print k, desired_nimber
		if desired_nimber == 0:
			memo[(k, desired_nimber)] = 1
			return (True, 1)
		else:
			memo[(k, desired_nimber)] = 0
			return (True, 0)
	child1_nimber = nimber(k - 1)
	child2_nimber = nimber(k - 2)
	total = 0
	# Either we lop off a child entirely, or there's some way to do it recursively.
	
	if child2_nimber + 1 == desired_nimber:
		total += 1
	if child1_nimber + 1 == desired_nimber:
		total += 1
	
	# the nimber of this tree is (child1_nimber + 1) ^ (child2_nimber + 1), so we must have
	# (chil1_nimber + 1) ^ (child2_nimber + 1) == desired_nimber, or
	# child1_nimber = (desired_nimber ^ (child2_nimber + 1)) - 1
	k_minus_one_nimber = (desired_nimber ^ (child2_nimber + 1)) - 1
	k_minus_two_nimber = (desired_nimber ^ (child1_nimber + 1)) - 1
	if (k - 1, k_minus_one_nimber) not in memo:
		if k_minus_one_nimber <= max_reachable_nimbers[k - 1]:
			return (False, (k - 1, (desired_nimber ^ (child2_nimber + 1)) - 1))
	if (k - 2, k_minus_two_nimber) not in memo:
		if k_minus_two_nimber <= max_reachable_nimbers[k - 2]:
			return (False, (k - 2, (desired_nimber ^ (child1_nimber + 1)) - 1))

	if k_minus_one_nimber <= max_reachable_nimbers[k - 1]:
		total += number_of_ways_to_make(k - 1, k_minus_one_nimber)[1]
	if k_minus_two_nimber <= max_reachable_nimbers[k - 2]:
		total += number_of_ways_to_make(k - 2, k_minus_two_nimber)[1]

	# print k, desired_nimber, total

	memo[(k, desired_nimber)] = total % modulus
	return (True, total % modulus)


def T(k):
	stack = [(k, 0)]
	while True:
		next_calculation = stack.pop()
		result = number_of_ways_to_make(next_calculation[0], next_calculation[1])
		if not result[0]:
			# Memoized data was insufficient.
			stack.append(next_calculation)
			stack.append(result[1])
		else:
			if len(stack) == 0:
				return result[1]

limit = 10000

reachable_nimbers_2_before = set()
reachable_nimbers_1_before = set([0])
max_reachable_nimbers = [0, 0, 0]
for i in range(3, limit + 1):
	child1_nimber = nimber(i - 1)
	child2_nimber = nimber(i - 2)
	current_reachable_nimbers = set([child1_nimber + 1, child2_nimber + 1])
	current_reachable_nimbers = current_reachable_nimbers.union({(nimber + 1) ^ (child2_nimber + 1) for nimber in reachable_nimbers_1_before})
	current_reachable_nimbers = current_reachable_nimbers.union({(nimber + 1) ^ (child1_nimber + 1) for nimber in reachable_nimbers_2_before})
	print i, len(current_reachable_nimbers)
	max_reachable_nimbers.append(max(current_reachable_nimbers))
	reachable_nimbers_2_before = reachable_nimbers_1_before
	reachable_nimbers_1_before = current_reachable_nimbers

# max_reachable_nimbers = [100000] * 100
# print max_reachable_nimbers

# print [(i, nimbers[i]) for i in range(len(nimbers)) if nimbers[i] > i]
# print [(i, nimber(i)) for i in range(1, 20)]
# a = [nimber(i) for i in range(1, 10000, 200)]
# print nimber(10000)

# a = [T(i) for i in range(1, 10000, 20)]
print T(limit)
# print number_of_ways_to_make(4, 3)