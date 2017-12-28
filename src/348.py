from math import sqrt
from collections import defaultdict

limit = 10**9

palindrome_counts = defaultdict(lambda : 0)

squares = [i**2 for i in range(int(sqrt(limit)))]
cubes = [i**3 for i in range(int(limit **(1.0 / 3)))]

def is_palindrome(s):
	return str(s) == ''.join(reversed(str(s)))

for square in squares:
	for cube in cubes:
		if square + cube > limit:
			break
		if is_palindrome(square + cube):
			palindrome_counts[square + cube] += 1

print sum([i for i in palindrome_counts.keys() if palindrome_counts[i] == 4])

# Runs in 40 seconds.
print sum([5229225, 37088073, 56200265, 108909801, 796767697])
'''
[56200265, 5229225, 37088073]
'''