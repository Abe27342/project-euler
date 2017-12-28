from cachetools import cached, LRUCache

# warning: this shit will EAT up your RAM. xD

cache = LRUCache(1000)

# returns a tuple (unique_sums, nonunique_sums) of all possible sums of the elements of A with size n.
@cached(cache)
def sums(A, n):
	assert len(A) >= n	
	if n == 0:
		return (frozenset([0]), frozenset())
	if len(A) == n:
		return (frozenset([sum(A)]), frozenset())

	cur_elem = A.__iter__().next()
	recurse_A = frozenset({i for i in A if i != cur_elem})
	(unique_sums1, nonunique_sums1) = sums(recurse_A, n)
	(unique_sums2, nonunique_sums2) = sums(recurse_A, n - 1)
	unique_sums2 = {i + cur_elem for i in unique_sums2}
	nonunique_sums2 = {i + cur_elem for i in nonunique_sums2}

	all_sums = unique_sums1.union(unique_sums2).union(nonunique_sums1).union(nonunique_sums2)
	unique_sums = (unique_sums1 ^ unique_sums2) - nonunique_sums1 - nonunique_sums2
	nonunique_sums = all_sums - unique_sums
	return (unique_sums, nonunique_sums)

B = [i ** 2 for i in range(1, 101)]
n = 50

unique, nonunique = sums(frozenset(B), n)
print sum(unique)