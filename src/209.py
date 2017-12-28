from itertools import product
from helpers import memoize

def next(input):
	a, b, c, d, e, f = input
	return (b, c, d, e, f, a ^ (b and c))


inputs = set(product([0, 1], repeat = 6))
cycles = []
while len(inputs) > 0:
	current_cycle = [inputs.pop()]
	while next(current_cycle[-1]) != current_cycle[0]:
		current_cycle.append(next(current_cycle[-1]))
	cycles.append(current_cycle)
	inputs -= set(current_cycle)

print cycles
print [len(cycle) for cycle in cycles]

# Surprisingly, the graph decomposes entirely as cycles.
# Their lengths are 46, 6, 6, 3, 1, 2.
'''
The 1 cycle must take on the value 0.
The 2 cycle has 3 possible options: 00, 10, or 01.
The 3 cycle has 4 possible options: 000, 100, 010, 001

In general, the n-cycle just must satisfy the constraint that no two ones are consecutive, including at the start/end.

let C(n) be the number of ways to do this.
Let A(n) be the number of ways to have no two consecutive ones, but the beginning and end are not counted as connected.

Then every element in C(n) either has a 1 as the first element, in which case it has a 0 as the second and last elements, and some
string of A(n-3) as the other ones
OR it has a 0 as the first element, in chich case it has some string in A(n - 1) as the other ones.

Every element of A(n) has a 1 as the first, in which case A(n-2) as others
OR it has a 0 as first, in which case A(n-1) as others.


'''

@memoize
def C(n):
	if n == 1:
		return 1
	elif n == 2:
		return 3
	elif n == 3:
		return 4
	else:
		return A(n - 3) + A(n - 1)

@memoize
def A(n):
	if n == 1:
		return 2
	elif n == 2:
		return 3
	else:
		return A(n - 2) + A(n - 1)

print reduce(lambda a, b: a * b, [C(len(cycle)) for cycle in cycles])