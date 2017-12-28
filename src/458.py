from helpers import fast_power, mult

n = 10 ** 12
modulus = 10 ** 9

A = [[1, 1, 1, 1, 1, 1], [6, 1, 1, 1, 1, 1], [0, 5, 1, 1, 1, 1], [0, 0, 4, 1, 1, 1], [0, 0, 0, 3, 1, 1], [0, 0, 0, 0, 2, 1]]
x1 = [[7], [0], [0], [0], [0], [0]]

# n - 1 since we have x1 instead of x0.
print sum([i[0] for i in mult(fast_power(A, n - 1, modulus), x1, modulus)]) % modulus