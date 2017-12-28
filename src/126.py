'''

The number of cubes in the nth layer of a cuboid with sides a,b,c is

2(ab + bc + ac) + 4(n-1)(a + b + c + n - 2).

'''
from itertools import combinations_with_replacement

def num_cubes(a, b, c, n):
	return 2 * (a * b + b * c + a * c) + 4 * (n - 1) * (a + b + c + n - 2)


class DictCounter:

	def __init__(self):
		self._dict = {}

	def get_dict(self):
		return self._dict

	def increment(self, key):
		if key in self._dict:
			self._dict[key] += 1
		else:
			self._dict[key] = 1


N = 20000

dictCounter = DictCounter()

for a in range(1, N):
	print a
	if num_cubes(a, a, a, 1) > N:
		break
	for b in range(a, N):
		if num_cubes(a, b, b, 1) > N:
			break
		for c in range(b, N):
			if num_cubes(a, b, c, 1) > N:
				break
			n = 1
			while num_cubes(a, b, c, n) <= N:
				dictCounter.increment(num_cubes(a, b, c, n))
				n += 1
print max(dictCounter.get_dict().values())
if 1000 in dictCounter.get_dict().values():
	print '1000 found!!'
	print [k for k in dictCounter.get_dict().keys() if dictCounter.get_dict()[k] == 1000]

print dictCounter.get_dict()[154]