'''

let 
a = m^2 - n^2
b = 2mn
c = m^2 + n^2

(We know it takes this form since the triple is primitive so we don't need to multiply by constants)

Since the triple has to be perfect, we need c = d^2 for some d.

Then d^2 = m^2 + n^2

so let

m = x^2 - y^2
n = 2xy
d = x^2 + y^2

'''
from helpers import gcd
from math import sqrt

c_limit = 10**8
d_limit = int(sqrt(c_limit))
xy_limit = int(sqrt(d_limit))


total = 0
for y in range(1, xy_limit + 1):
	#if y % 10 == 0:
	#	print y
	for x in range(y + 1, xy_limit + 1, 2):
		if gcd(x, y) == 1:
			m = x * x - y * y
			n = 2 * x * y
			d = x * x + y * y
			if gcd(m, n) == 1 and (m % 2 == 0 or n % 2 == 0) and d * d <= c_limit:
				a = abs(m * m - n * n)
				b = 2 * m * n 
				area = a * b / 2
				if area % 28 != 0 and area % 6 != 0:
					total += 1

print total

'''

LOL IT'S 0


'''