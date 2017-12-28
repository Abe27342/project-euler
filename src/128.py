'''
For n > 1, the only possible tiles are the first tiles of a given ring (which can be proven rather easily by explicitly calculating the adjacent differences)
or the last tiles of a given ring.

also, P(1) = P(2) = 3.

For n > 1, P(3n^2 - 3n + 2) = 3 if and only if 6n-1, 6n+1, and 12n+5 are all prime.
also, P(3(n+1)^2 - 3(n+1) + 1) = 3 if and only if 6n - 1, 6n + 5, and 12n - 7 are all prime.
'''
from helpers import isPrimeMR as is_primeMR

N = 2000

i = 2

values = [1, 2]
n = 2
while len(values) < N:
	if is_primeMR(6 * n - 1) and is_primeMR(6 * n + 1) and is_primeMR(12 * n + 5):
		values.append(3 * n * n - 3 * n + 2)
		# print 3 * n * n - 3 * n + 2
	if is_primeMR(6 * n - 1) and is_primeMR(6 * n + 5) and is_primeMR(12 * n - 7):
		values.append(3 * (n + 1) * (n + 1) - 3 * (n + 1) + 1)
		# print 3 * n * n - 3 * n + 1
	n += 1

values = sorted(values)
print values
print values[-1]

