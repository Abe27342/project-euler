
a = 21**7
b = 7**21
c = 12**7
modulus = 10**9

def F(n):
	if n > b:
		return n - c
	else:
		return F(a + F(a + F(a + F(a + n))))

# m = b - a
# s = c - a
# k = a
def M(n):
	if n > m:
		return n - s
	else:
		return M(M(n + k))

'''

goes down by  (k - s) when going from m to m + 1
as well as from m - (k - s) * some_integer to (m - (k - s) * that integer + 1)

ALSO always increases by 1.



'''

def fast_M(n):
	value_at_m_plus_1 = m + 1 - s
	num_one_increases = m + 1 - n 
	num_jumps = 1 + (m - n) / (k - s)
	total_decreases = num_jumps * (k - s)
	return value_at_m_plus_1 - num_one_increases + total_decreases

def short_M(n):
	return n - s + (k - s) * (1 + (m - n)/(k - s))

def SF():
	return sum([fast_M(i) for i in range(m + 1) if fast_M(i) == i])

def fast_SF():
	a = k - s 
	qa = 2 * s - k
	if qa % a != 0:
		return 0
	else:
		return m * a - qa * a - a * (a - 1) / 2

def S(p, m):
	total = 0
	for a in range(1, p):
		r = p/a - 1
		total += r * (m * a - a * (a - 1) / 2) - a * a * r * (r - 1) / 2

	return total

m = 1000
k = 500
s = 400
print S(10**6, 10**6)
'''

print 2 * s - k
print (k - s) * (( m - 91) / (k - s))

print SF()
print fast_SF()

The problem comes down to finding the sum of solutions to

2s - k = (k - s) * floor((m - n) / (k - s)) for a fixed m.

Let a = k - s and b = 2s - k. Then we have a divides b, and 
solving the equations with the constraint 1 <= s < k <= p gives



'''