from itertools import permutations


def to_base_10(n, old_base):
	return reduce(lambda a, b: old_base * a + b, n)

def from_base_10(n, new_base):
	answer = []
	while n > 0:
		answer.append(n % new_base)
		n /= new_base
	answer = reversed(answer)
	return [i for i in answer]

def is_pandigital(n_base_10, base):
	return len(set(from_base_10(n_base_10, base))) == base

def is_12_super_pandigital(n):
	for base in range(2, 13):
		if not is_pandigital(n, base):
			return False
	return True

print sum([1587937206284,
1674839888205,
2638904175622,
2806980157234,
2816957039424,
3325871906940,
3863090145827,
3909765781284,
3925260871994,
3960783529164])

for perm in permutations([i for i in range(12)]):
	if perm[0] == 0:
		continue
	if is_12_super_pandigital(to_base_10(perm, 12)):
		print perm, to_base_10(perm, 12)


'''
First few are:
1587937206284
1674839888205
2638904175622
2806980157234
2816957039424
3325871906940
3863090145827
3909765781284
3925260871994
3960783529164


'''