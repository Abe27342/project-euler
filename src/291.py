'''

It can be shown that we need to have xy = k(k+1)^2 and x - y = k + 1 in order to get an integer that is potentially prime,
and this potentially prime number is 2k + 1.

Letting alpha = x - y and beta = x + y, we can further transform this to 
beta^2 = alpha^2(4alpha - 3), where the prime is 2 * alpha - 1.

Since x > y, we have alpha in the range from 1 to (limit + 1) / 2 inclusive

But this still gives linear runtime. So to get the sqrt(n) runtime required for the given limit, we only iterate over odd squares

for a given odd value of i, set i^2 = 4alpha - 3.
Then alpha can be at most (limit + 1) / 2, so 4alpha - 3 is at most 2 * (limit + 1) - 3
or 2 * limit - 1


4037526
[Finished in 1651.7s]
'''
from math import sqrt
from helpers import isPrimeMR

limit = 5 * 10**15

count = 0

for i in xrange(1, int(sqrt(2 * limit)), 2):
	if i % 100000 == 1:
		print i, int(sqrt(2 * limit))
	alpha = (i * i + 3) / 4
	if isPrimeMR(2 * alpha - 1):
		# print 2 * alpha - 1
		count += 1

print count