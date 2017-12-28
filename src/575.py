'''

Steady state can be found by intution. For one prob distribution, it's 2 for corners, 3 for edges, 4 for middle.
For the other, it's 3 for corners, 4 for edges, 5 for middle.


'''
from math import sqrt

def normalizing_constant_1(m, n):
	return 4 * 2  + 2 * (m + n - 4) * 3 + (m - 2) * (n - 2) * 4

def normalizing_constant_2(m, n):
	return 4 * 3  + 2 * (m + n - 4) * 4 + (m - 2) * (n - 2) * 5

def is_corner(i, j, m, n):
	return i in [0, m - 1] and j in [0, n - 1]

def is_edge(i, j, m, n):
	return not is_corner(i, j, m, n) and (i in [0, m - 1] or j in [0, n - 1])


m = 1000
n = 1000
squares = [i*i for i in range(int(sqrt(m * n)) + 1)]


total_1 = 0
total_2 = 0
total3 = 0
for i in range(m):
	for j in range(n):
		square_num = 1 + m * i + j
		if square_num in squares:
			if is_corner(i, j, m, n):
				total_1 += 2
				total_2 += 3
			elif is_edge(i, j, m, n):
				total_1 += 3
				total_2 += 4
			else:
				total_1 += 4
				total_2 += 5

total = float(total_1) / normalizing_constant_1(m, n) + float(total_2) / normalizing_constant_2(m, n)
total /= 2

print total
