
a = 21**7
b = 7**21
c = 12**7
modulus = 10**9

def F(n):
	if n > b:
		return n - c
	else:
		return F(a + F(a + F(a + F(a + n))))

def g(n):
	if n > b - a:
		return n + a - c
	else:
		return g(g(g(g(n + a))))

def fast_F(n):
	'''
	at b + 1, function value is b + 1 - c.
	
	'''
	value_before_jumps = n - c
	'''
	Always at least one jump going up, then after that 
	'''

	num_jumps = 1 + (b - n) / a 
	value_accounting_for_jumps = value_before_jumps + num_jumps * (4 * a - 3 * c)
	return value_accounting_for_jumps


def S(n):
	return sum([F(i) for i in range(n + 1)])

def fast_S(n):
	answer = 4 * (n + 1) * (a - c) + (n * (n + 1)) / 2
	biggest_term = n / a
	number_of_biggest_terms = (n % a) + 1
	answer += (4 * a - 3 * c) * biggest_term * number_of_biggest_terms
	# add all smaller terms
	answer += ((4 * a - 3 * c) * a * (biggest_term - 1) * biggest_term) / 2
	answer %= modulus
	return answer

#print #S(2000), fast_S(2000)

print fast_S(b)

'''
It appears that F increases by 1 when going from k to k + 1, unless k is of the form b - a * n for n an integer, in which case
it goes down by 4 * a - 3 * c and then increases by 1

This amount is determined by the value of F(b), so if we just try to compute:

F(b) = F(a + F(a + F(a + F(a + b))))
	 = F(a + F(a + F(a + a + b - c)))
	 = F(a + F(a + F(b - c)))
let g(x) = F(a + x).
Then

F(b) = g^4(b)

Also, evidently g(n) = n + a - c if n + a > b.
So g(n) = n + (a - c)  if n > (b - a).
Otherwise, g(n) = g^4(n + a).


'''

#print [(i, F(i), F(i) - F(i + 1))  for i in range(1500, 2001) if F(i + 1) - F(i) != 1]
#print [(i, F(i), fast_F(i)) for i in range(1900, 2001) if F(i) != fast_F(i)]
#print [(i, g(i - a), g(i - a) - g(i - a + 1)) for i in range(1500, 2001) if F(i + 1) - F(i) != 1]
#print F(2000)
#print g(2000-a)
#print F(b), g(g(g(g(b)))), b + 4 * (a - c)
