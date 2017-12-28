from helpers import prime_factorizations, sieve, euler_totient
from bisect import bisect_right

limit = 10**8

def find_le_index(a, x):
    'Find rightmost index i with a[i] less than or equal to x'
    i = bisect_right(a, x)
    if i:
        return i-1
    raise ValueError

primes = sieve(limit)
setprimes = set(primes)
pfs = prime_factorizations(limit / 100)

print 'done getting initial bs'

def get_pf(n):
    if n < len(pfs):
        return pfs[n]
    else:
        if n in setprimes:
            return {n : 1}
        ans = {}
        for p in primes:

            if n < len(pfs) or n in setprimes:
                break
            power = 0
            while n % p == 0:
                power += 1
                n /= p 

            if power > 0:
                ans[p] = power 

        if n in setprimes:
            ans[n] = 1
        elif n > 1:
            recursive_ans = {k : v for (k, v) in pfs[n].items()}
            for (prime, power) in ans.items():
                if prime in recursive_ans:
                    recursive_ans[prime] += power
                else:
                    recursive_ans[prime] = power

            return recursive_ans 

        return ans

# returns the order of a modulo n. Assumes a and n are relatively prime.
def order(a, n):
	biggest_order = euler_totient(get_pf(n))
	pf = get_pf(biggest_order)

	current_order = biggest_order
	for prime in pf.keys():
		while current_order % prime == 0 and pow(a, current_order, n) == 1:
			current_order /= prime 

		if pow(a, current_order, n) != 1:
			current_order *= prime 
		assert pow(a, current_order, n) == 1

	return current_order

powers_of_two_and_five = []
p2 = 0
while 2**p2 < limit:
	p5 = 0
	while 2**p2 * 5**p5 < limit:
		powers_of_two_and_five.append(2**p2 * 5**p5)
		p5 += 1
	p2 += 1

powers_of_two_and_five = sorted(powers_of_two_and_five)

print order(10, 1539)

print powers_of_two_and_five
print [(i, find_le_index(powers_of_two_and_five, i)) for i in range(1, 10)]
total = 0

max_value = limit
for n in range(3, max_value + 1):
	if n % 10000 == 0:
		print n
	if n % 2 != 0 and n % 5 != 0:
		cycle_length = order(10, n)
		number_of_nums = find_le_index(powers_of_two_and_five, float(max_value) / n) + 1
		# print (n, cycle_length, number_of_nums)
		total += cycle_length * number_of_nums

print total