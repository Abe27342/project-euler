from helpers import prime_factorizations

pfs = prime_factorizations(1000)

def pf_divisors(pf):
	if len(pf) == 0:
		yield 1
		return
	prime, power = pf.popitem()
	for divisor in pf_divisors(pf):
		for i in range(power + 1):
			yield divisor * prime**i

	pf[prime] = power

def divisors(n):
	pf = pfs[n]
	for i in pf_divisors(pf):
		yield i

def proper_divisors(n):
	for divisor in divisors(n):
		if divisor != n:
			yield divisor

def smallest_number_not_in_set(s):
	i = 0
	while i in s:
		i += 1
	return i

print [i for i in divisors(24)]

nimbers = [0, 0]
for i in range(2, 101):
	covered_nimbers = set([nimbers[i - j] for j in proper_divisors(i)])
	next_nimber = smallest_number_not_in_set(covered_nimbers)
	nimbers.append(next_nimber)

print [(i, nimbers[i]) for i in range(101)]

'''

The above line suggests that the nimber of a stone pile in divisor nim of size n is v_2(n).
This makes a reasonable amount of sense, so I won't bother proving it. It shouldn't be too hard though.

'''

modulus = 1234567890
def S(n):
	# number_of_nimbers[i] contains the number of nimbers that are 'i' in the range [1, n].
	number_of_nimbers = []
	cur_n = n 
	while cur_n > 0:
		number_of_nimbers.append(cur_n - cur_n / 2)
		cur_n /= 2

	total = 0
	m = len(number_of_nimbers)
	for a in range(m):
		for b in range(m):
			for c in range(m):
				if a ^ b ^ c != 0:
					total += number_of_nimbers[a] * number_of_nimbers[b] * number_of_nimbers[c]
					total %= modulus
	return total



print S(123456787654321)