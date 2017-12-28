from itertools import product
from helpers import sieve

def digit_sum(n):
	return sum([int(i) for i in str(n)])

# num_transitions[i] returns the number of segments used in the number i.
num_transitions = [6, 2, 5, 5, 4, 5, 6, 4, 7, 6]
num_segments_lit = [{1, 2, 3, 5, 6, 7}, {3, 6}, {1, 3, 4, 5, 7}, {1, 3, 4, 6, 7}, {2, 3, 4, 6}, {1, 2, 4, 6, 7}, {1, 2, 4, 5, 6, 7}, {1, 2, 3, 6}, {1, 2, 3, 4, 5, 6, 7}, {1, 2, 3, 4, 6, 7}]
num_transition_paired = {(i, j) : len(num_segments_lit[i] ^ num_segments_lit[j]) for (i,j) in product(range(10), repeat = 2)}


# returns the number of transitions sam uses to write out all the digital roots of n.
def sam_transitions_required(n):
	answer = 0
	while digit_sum(n) != n:
		answer += 2 * sum([num_transitions[int(i)] for i in str(n)])
		n = digit_sum(n)
	answer += 2 * sum([num_transitions[int(i)] for i in str(n)])
	return answer

def smart_transitions_required(n, m):
	assert n > m
	answer = 0
	n = [i for i in str(n)]
	m = [i for i in str(m)]
	while len(n) > len(m):
		answer += num_transitions[int(n[0])]
		n = n[1:]
	for i in range(len(n)):
		num1 = int(n[i])
		num2 = int(m[i])
		answer += num_transition_paired[(num1, num2)]
	return answer

def max_transitions_required(n):
	answer = 0
	answer += sum([num_transitions[int(i)] for i in str(n)])
	while digit_sum(n) != n:
		answer += smart_transitions_required(n, digit_sum(n))
		n = digit_sum(n)
	answer += sum([num_transitions[int(i)] for i in str(n)])
	return answer

primes = [p for p in sieve(2 * 10 ** 7) if p > 10 ** 7]
print 'primes found'
answer = 0
for p in primes:
	answer += sam_transitions_required(p) - max_transitions_required(p)

print answer
# print sam_transitions_required(137)
# print max_transitions_required(137)