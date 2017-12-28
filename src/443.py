'''

Simulation for a bit.


'''
from helpers import gcd, memoize


@memoize
def g(n):
	if n == 4:
		return 13
	else:
		if gcd(n, g(n-1)) != 1:
			print n, g(n - 1), gcd(n, g(n - 1))
		return g(n - 1) + gcd(n, g(n - 1))

a = {n : g(n) - n for n in range(4, 1000)}
b = [k for (k, v) in a.items() if k+1 in a and v != a[k + 1]]

print b

'''

Seems like it might just be brute force while storing the current difference g(n) - n.

Let f(n) = g(n) - n.

Then f(n) = g(n-1) + gcd(n, g(n - 1)) - n
          = f(n-1) - 1 + gcd(n, f(n-1) + n - 1).
          = f(n-1) - 1 + gcd(n, f(n-1) - 1)

So f(n) is constant unless gcd(n, f(n-1) - 1) is not 1.
This suggests we prime factorize f(n-1) - 1 at each step       