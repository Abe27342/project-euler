from helpers import isPrimeMR


N = 50000000

total = 0
for k in xrange(2, N + 1):
	if isPrimeMR(2 * k * k - 1):
		total += 1

print total