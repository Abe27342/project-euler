from itertools import combinations


def type_1(i, j, m, n):
	return (i - j) * (2 * m - 2 * i - 1) + (i - j + 1) * (i - j) / 2


def type_2(i, j, m, n):
	return (2 * m - i - j) * (2 * m - i - j - 1) / 2

def type_3(i, j, m, n):
	return type_1(n + j, i - n, m, n)

def type_4(i, j, m, n):
	return (i - j) * (2 * m - 2 * i - 1) + (2 * n + j - i) * (2 * m - 2 * n - 2 * j - 1) + (2 * n - 2 * m + i + j + 2) * (2 * n - 2 * m + i + j + 1) / 2 - (2 * m - 2 * i - 1) * (2 * m - 2 * n - 2 * j - 1)


# l m f a o    look at this bullshit
def num_cross_hatched(m, n):
	if m > n:
		return num_cross_hatched(n, m)
	total = 0
	for i in range(m + n + 1):
		for j in range(max(-i, i - 2 * n), min(i, 2 * m - i)):
			if i < m and j >= m - n:
				total += type_1(i, j, m, n)
			elif i >= m and j >= m - n:
				total += type_2(i, j, m, n)
			elif i >= m and j < m - n:
				total += type_3(i, j, m, n)
			elif i < m and j < m - n:
				total += type_4(i, j, m, n)
	return total

def num_vertical(m, n):
	return (n + 1) * n * (m + 1) * m / 4

def num_rectangles(m, n):
	return num_vertical(m, n) + num_cross_hatched(m, n)


M = 47
N = 43
# print type_4(2, -2, 3, 4)
total = 0
for m in range(1, M + 1):
	for n in range(1, N + 1):
		total += num_rectangles(m, n)
print total



def is_type_4(i, j, m, n):
	return i < m and j < m - n

def satisfies_bounds(i, j, m, n):
	return max(-i, i - 2 * n) <= j <= min(i, 2 * m - i) 

def forms_rectangle(point1, point2, m, n):
	i1,j1 = point1
	i2,j2 = point2
	if not is_type_4(i1, j1, m, n) and not is_type_4(i2, j2, m, n) and not is_type_4(i1, j2, m, n) and not is_type_4(i2, j1, m, n):
		return False
	return satisfies_bounds(i1, j2, m, n) and satisfies_bounds(i2, j1, m, n) and i1 != i2 and j1 != j2

# brute forces number of cross-hatched rectangles 
def fuck_this_gay_earth(m, n):
	if m > n:
		return fuck_this_gay_earth(n, m)
	points = []
	for i in range(m + n + 1):
		for j in range(max(-i, i - 2 * n), min(i, 2 * m - i) + 1):
			points.append((i,j))

	total = 0
	for point1,point2 in combinations(points, 2):
		if forms_rectangle(point1, point2, m, n):
			#print point1,point2
			total += 1
	return total / 2

# print num_cross_hatched(M, N)
print fuck_this_gay_earth(M, N)

# print type_4(2, -2, 3, 4)
# print type_4(2, -2, 3, 3)
