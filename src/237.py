

def solve_recurrence(coeffs, x0, n, modulus):
	xn = mult(fast_power(recurrence_matrix(coeffs), n, modulus), x0, modulus)
	return xn[-1][0]

# multiplies the matrices A and B, represented as double lists and taken modulo the modulus
# if modulus is -1, ignores.
def mult(A, B, modulus):
	common_dim = len(A[0])
	m = len(A)
	n = len(B[0])
	assert len(A[0]) == len(B)

	#product is an m by n matrix
	product = [[0 for i in range(n)] for j in range(m)]
	for i in range(m):
		for j in range(n):
			for k in range(common_dim):
				product[i][j] += A[i][k] * B[k][j]
				if modulus != -1:
					product[i][j] %= modulus
	return product

def fast_power(A, n, modulus):
	if n == 1:
		return A
	halfA = fast_power(A, n // 2, modulus)
	
	if n % 2 == 0:
		return mult(halfA, halfA, modulus)
	else:
		return mult(mult(halfA, halfA, modulus), A, modulus)

# For a recurrence of the form a_n = \sum c_{n-i} a_{n-i}, the coeffs list should be [c_{n-1}, c_{n-2}, \cdots].
def recurrence_matrix(coeffs):
	A = [coeffs]
	A.extend([[0 for i in range(len(coeffs))] for j in range(len(coeffs) - 1)])
	for i in range(len(coeffs) - 1):
		A[i + 1][i] = 1
	return A




memo = {0: 0, 1: 1, 2: 1}

def T(n):
	if n in memo:
		return memo[n]
	ans = 1
	ans += 3 * T(n - 2)
	for i in xrange(3, n):
		ans += (i - 1) * 2 * T(n - i)
	memo[n] = ans
	return ans


# T(n) = 2 T(n - 1) + 2 T(n - 2) - 2 T(n - 3) + T(n - 4)

# x^4 - 2 x^3 - 2x^2 + 2x - 1

def improved_T(n, modulus):
	#recent_tn[i] = T(n - i).
	tn_cur = 0
	tn_last = 0
	tn_sum = 0
	tn_weighted_sum = 0
	for n_cur in xrange(0, n):
		# at start of loop, recent_tn is accurate, and:
		# tn_sum = T(n_cur) + T(n_cur - 1) + ... + T(1)
		# tn_weighted_sum = 0 T(n - 1) + 2 T(n - 2) + ... + 2(i-1)T(n - i)
		
		#T(n + 1) = 1 + T(n - 1) + 2 T(n - 1) + 4 T(n - 2) + 6 T(n - 3) + ...
		tn_next = 1 + tn_last + tn_weighted_sum + 2 * (tn_sum - tn_cur)
		tn_weighted_sum = (tn_weighted_sum + 2 * (tn_sum - tn_cur)) % modulus
		tn_sum = (tn_sum + tn_next) % modulus
		tn_last = tn_cur
		tn_cur = tn_next % modulus
#		if n_cur % 10**6 == 0:
#			print n_cur
	# Now T(n) = 1 + 3 T(n - 2) + 4 T(n - 3) + 6 T(n - 4) + ...


	return tn_cur

def f(n):
	assert n >= 2
	return improved_T(n + 2, 10**8) - 2 * improved_T(n + 1, 10**8) - 2 * improved_T(n, 10**8) + 2 * improved_T(n - 1, 10**8) - improved_T(n - 2, 10**8)


for i in range(10):
	print T(i), improved_T(i, 10**8)

print improved_T(10**6, 10**8)




A =  recurrence_matrix([1, 1])
x0 = [[improved_T(i, 10**8)] for i in range(3, -1, -1)]
print x0
print solve_recurrence([2, 2, -2, 1], x0, 10**12, 10**8)
print improved_T(5, 10**8)