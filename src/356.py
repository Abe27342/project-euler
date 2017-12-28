'''

let g_n(x) = x^3 - 2^n x^2 + n.

then g_n has a root that is roughly 2^n (in fact, a little less), a root in (0, 1), and a root in (-1, 0).

The positive root is larger in sign than the negative root.

So the sum of the three roots to the 987654321th power is very close to a_n^987654321.

In fact, the former sum is an *integer*, and it's larger than the latter sum because the positive root is larger
in absolute value than the negative root.


So if S_k = r_1^k + r_2^k + r_3^k, where r_i's are the roots, we have the answer is S_{987654321} - 1.

furthermore,

S_1 = 2^n 
1 S_2 - 2^n S_1 = 0, so S_2 = 4^n 
S_3 - 2^n S_2 + 3n = 0, so S_3 = 8^n - 3n

from then on, S_n - 2^n S_{n-1} + n S_{n - 3} = 0, so S_n = 2^n S_{n - 1} - n S_{n - 3}

'''
from helpers import solve_recurrence


# returns floor(a_n^power), assuming power is sufficiently high.
def sum_term(n, power):
	newton_sum = solve_recurrence([2**n, 0, -n], [[8**n - 3 * n], [4**n], [2**n]], power - 1, 10**8)
	return newton_sum - 1


print sum([sum_term(i, 987654321) for i in range(1, 31)]) % 10**8

print sum_term(4, 5)