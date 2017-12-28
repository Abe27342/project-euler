

from helpers import solve_recurrence


coeffs = [0] * 1998 + [1, 1]
x0 = [[1] for i in range(2000)]
modulus = 20092010

print solve_recurrence(coeffs, x0, 1, modulus)