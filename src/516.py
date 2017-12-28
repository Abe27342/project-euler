from helpers import isPrimeMR




hamming_number_factor_start = [2, 3, 5]
limit = 10**12
allowable_primes = []

p2 = 0
while 2**p2 < limit:
	p3 = 0
	while 2**p2 * 3**p3 < limit:

		p5 = 0
		while 2**p2 * 3**p3 * 5**p5 < limit:
			num = 2**p2 * 3**p3 * 5**p5
			if isPrimeMR(num + 1):
				allowable_primes.append(num + 1)
			p5 += 1


		p3 += 1

	p2 += 1

allowable_primes.remove(2)
allowable_primes.remove(3)
allowable_primes.remove(5)
allowable_primes = sorted(allowable_primes)
allowable_primes = [i for i in reversed(allowable_primes)]
print allowable_primes
def S_with_given_235(num, list_to_consider):
	if num > limit:
		return 0
	if len(list_to_consider) == 0:
		return num
	total = 0
	it = list_to_consider.pop()
	if num * it > limit:
		list_to_consider.append(it)
		return num
	total += S_with_given_235(num * it, list_to_consider)
	total += S_with_given_235(num, list_to_consider)
	list_to_consider.append(it)
	return total

total = 0
p2 = 0
while 2**p2 <= limit:
	print p2
	p3 = 0
	while 2**p2 * 3**p3 <= limit:

		p5 = 0
		while 2**p2 * 3**p3 * 5**p5 <= limit:
			num = 2**p2 * 3**p3 * 5**p5
			total += S_with_given_235(num, allowable_primes)

			p5 += 1

		p3 += 1

	p2 += 1


print len(allowable_primes)

print total
'''
Gives 15058726287897613779

need to take this mod 2**32 to get real answer. I forgot about that.

'''