'''

if r_a, r_b, and r_c are x, y, and z respectively, then we want to find integer solutions to

sqrt(xz) + sqrt(yz) = sqrt(xy).

Evidently, this means xz, yz, and xy all have the same squarefree number as their base.
In fact, we need to have sqrt(xy) is an integer and therefore sqrt(xz) and sqrt(yz) need to be integers as well.

This is because squaring the equation gives
z(x + y + 2sqrt(xy)) = xy, hence z = xy/(x + y + 2sqrt(xy)).

So xz, yz, and xy need to all be perfect squares.

Since xy is an integer, this means x, y, and z are all some integer multiple of a solution in which x, y, and z are perfect squares. So let

x = a^2, y = b^2, z = c^2

Then ac + cb = ab, so c(a + b) = ab.

this should put us in brute force range of the limit, as now a and b are at most sqrt(10^9) and c is determined by a and b.
:)


'''
from math import sqrt
from helpers import gcd

limit = 10**9

sqrootlimit = int(sqrt(limit))


total = 0
for a in range(1, sqrootlimit + 1):
	if a % 10 == 0:
		print a
	for b in range(a, sqrootlimit + 1):
		if a * b % (a + b) == 0:
			c = a * b / (a + b)
			if gcd(gcd(a, b), c) == 1:
				x = a * a 
				y = b * b 
				z = c * c
				max_allowable_multiple = limit / y
				# print x,y,z 
				total += max_allowable_multiple * (max_allowable_multiple + 1) * (x + y + z) / 2


print total

'''
315306518862563689
[Finished in 134.3s]
'''