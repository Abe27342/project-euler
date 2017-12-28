from helpers import memoize, gcd
from itertools import permutations

@memoize
def fact(n):
	if n == 0:
		return 1
	else:
		return n * fact(n - 1)

def f(m, n):
	total = 0
	for k in range(1, n + 1):
		# print k
		total += fact(m * gcd(n, k)) / (fact(gcd(n, k))**m)
	return total / (m * n)

def rotations(p):
	return {p[i:] + p[:i] for i in range(len(p))}

def slow_f(m, n):
	toppings = n * [i for i in range(m)]
	possibilities = set()
	for p in permutations(toppings):
		if rotations(p).intersection(possibilities) == set():
			possibilities.add(p)
	return len(possibilities)

limit = 10**15
m = 2
n = 1
vals = set()
total = 0
while f(m, n) <= limit:
	while f(m, n) <= limit:
		vals.add(f(m, n))
		total += f(m, n)
		n += 1	
	m += 1
	n = 1

print sum(vals)
print total
print f(2, 1), f(2, 2), f(3, 1), f(3, 2), f(3, 3)
# print slow_f(2, 1), slow_f(2, 2), slow_f(3, 1), slow_f(3, 2), slow_f(3, 3)
print slow_f(2, 5), f(2, 5)