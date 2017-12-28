
T = [[15], [-14, -7], [20, -13, -5], [-3, 8, 23, -26], [1, -4, -5, -18, 5], [-16, 31, 2, 9, 28, 3]]

N = 1000
T = [[0 for i in range(j + 1)] for j in range(N)]
t = 0
i,j = 0,0
for k in range(1, 500501):
	t = (615949*t + 797807) % (2 ** 20)
	T[i][j] = t - 2 ** 19
	if j < i:
		j += 1
	else:
		j = 0
		i += 1


print 'made array'
print T[0][0]
print T[1][0]
print T[1][1]
print [len(i) for i in T]


smallest_sum = min([min([i for i in j]) for j in T])

horizontal_row_sums = [[i for i in j] for j in T]
vertical_row_sums = [[i for i in j] for j in T]
diagonal_row_sums = [[i for i in j] for j in T]

# prev_triangle_sums[i][j] is sum of the triangle with side length d starting at upper left corner (i,j).
triangle_sums = [[i for i in j] for j in T]

N = len(T)
for d in range(2, N + 1):
	for i in range(d - 1, N):
		for j in range(i - d + 2):
			horizontal_row_sums[i][j] += T[i][j + d - 1]

	for i in range(N - d + 1):
		for j in range(i + 1):
			vertical_row_sums[i][j] += T[i + d - 1][j]
			diagonal_row_sums[i][j] += T[i + d - 1][j + d - 1]

	for i in range(N - d + 1):
		for j in range(i + 1):
			triangle_sums[i][j] += triangle_sums[i + 1][j] + triangle_sums[i + 1][j + 1] + vertical_row_sums[i][j] + diagonal_row_sums[i][j] + horizontal_row_sums[i + d - 1][j]
			assert triangle_sums[i][j] % 3 == 0
			triangle_sums[i][j] /= 3
			if triangle_sums[i][j] < smallest_sum:
				smallest_sum = triangle_sums[i][j]
	print d
	# print triangle_sums

print smallest_sum
