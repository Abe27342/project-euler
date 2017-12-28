
from helpers import sieve_euler_phi, crt, gcd, prime_factorizations

upper_limit = 10**6 + 5000
lower_limit = 10**6
print crt([(1, 2), (2, 3), (3, 5)])
euler_phi = sieve_euler_phi(upper_limit + 1)
pfs = prime_factorizations(upper_limit + 1)

def attempt_to_solve(a, n, b, m):
	d = gcd(n, m)
	reduced_a = a % d 
	reduced_b = b % d 
	if reduced_a != reduced_b:
		return 0
	else:
		n_pf = pfs[n]
		m_pf = pfs[m]
		L = []
		for (prime, power) in n_pf.items():
			if prime in m_pf and m_pf[prime] >= power:
				# do nothing for now
				r = 1
			else:
				L.append((a % (prime**power), prime**power))
		for (prime, power) in m_pf.items():
			if prime in n_pf and n_pf[prime] > power:
				# do nothing
				r = 1
			else:
				L.append((b % (prime**power), prime**power))

		answer = crt(L)
		return answer % (n * m / d)
print 'working through numbers now'
total = 0
for n in range(lower_limit, upper_limit):
	print n
	for m in range(n + 1, upper_limit):
		total += attempt_to_solve(euler_phi[n], n, euler_phi[m], m)
print total

print attempt_to_solve(2, 4, 4, 6)