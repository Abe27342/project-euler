'''
For each frog i, we compute the distribution of the square number it's on after 50 rings of the bell.

(takes forever to run, but works. Fucking python, man)
330.721154014
[Finished in 2651.8s]
'''

from helpers import mult, dirac

def are_adjacent(i1, j1, i2, j2):
	return (i1 == i2 and j1 in [j2 + 1, j2 - 1]) or (j1 == j2 and i1 in [i2 + 1, i2 - 1])

def prob(ser1, ser2, m, n):
	i1 = ser1 / m
	i2 = ser2 / m
	j1 = ser1 % m 
	j2 = ser2 % m
	if i1 == 0 or i1 == n - 1:
		if j1 == 0 or j1 == n - 1:
			prob_if_adjacent = 0.5
		else:
			prob_if_adjacent = 1.0 / 3
	else:
		if j1 == 0 or j1 == n - 1:
			prob_if_adjacent = 1.0 / 3
		else:
			prob_if_adjacent = 1.0 / 4

	if are_adjacent(i1, j1, i2, j2):
		return prob_if_adjacent
	else:
		return 0


def fast_power_iterative(A, n, modulus):
    result = [[dirac(i, j) for i in range(len(A))] for j in range(len(A))]
    
    while n > 0:
        print n
        if n % 2 == 1:
            result = mult(result, A, modulus)
        A = mult(A, A, modulus)
        n /= 2
    return result


def matrix(m, n):
	# Index the m * n possible states by m * i + j, where 0 \leq i < n, and 0 \leq j < m
	return [[prob(ser1, ser2, m, n) for ser1 in range(m * n)] for ser2 in range(m * n)]

m = 30
n = 30

A = matrix(m, n)
A_to_the_50 = fast_power_iterative(A, 50, 1000000)
# print A_to_the_50

answer = 0
for row in A_to_the_50:
	answer += reduce(lambda a, b : a * b, map(lambda x : 1 - x, row))


print 'done'
print answer

