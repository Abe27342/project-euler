
limit = 10 ** 12

squares = {i**2 for i in xrange(1, int(pow(limit, 0.5)))}

progressive_squares = set()
for numerator in xrange(2, int(pow(limit, 1.0/3.0))):
	for denominator in range(1, min(numerator, int(pow(limit, 0.5)))):
		r = denominator * denominator
		q = r * numerator / denominator
		d = r * numerator / denominator
		n = q * d + r
		if n >= limit:
			break
		for multiplier in xrange(1, int(pow(limit, 0.5))):
			r = multiplier * denominator * denominator
			q = r * numerator / denominator
			d = q * numerator / denominator
			n = q * d + r
			if n >= limit:
				break
			if n in squares:
				print n
				progressive_squares.add(n)

print sum(progressive_squares)

'''
# 97344 was missing. Why? cuz i sucked. It's fixed now.
N = 97344
for d in range(2, int(pow(N, 0.5))):
	q = N / d 
	r = N % d
	if r * q == d * d:
		print r,d,q

'''