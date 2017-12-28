'''
For disk i, the probability that it is flipped on any given turn is

given by p(i, N) below.

We want the probability that after M flips, the number of times this coin is flipped is even.

Let p = p(i, N)

then by roots of unity filter, we get that this probability is

(1 + (2*p - 1)^M)/2.


so over all N coins, the expected number that have been flipped an even number of times is:

\sum_{i = 1}^N (1 + (2*p - 1)^M)/2
= N/2 + 1/2 \sum_{i = 1}^N (2*p - 1)^M

11
12
13
21
22
23
31
32
33
first one flipped in 5 of the above
last one flipped in 5 of the above
second one flipped in 7 of the above


7000000
8000000
9000000
10000000
624921.322336
5000624921.32

'''




N = 10**10
M = 4000

precision = 10**(-8)

def p(i, N):
	return 1 - float((i - 1)**2)/(N * N) - float((N - i)**2)/(N * N)
	return float(i * (N - i + 1))/(N * N)

def actual_probability(i, n, m):
	p2 = p(i, n)
	return float(1 + pow(2 * p2 - 1, m)) / 2

i = 1

total = 0
while abs(pow(2 * p(i, N) - 1, M)) > precision and i <= N / 2:
	total += pow(1 - 2 * p(i, N), M)
	i += 1
	if i % 1000000 == 0:
		print i

if N % 2 == 1:
	print p(N / 2 + 1, N)
	print pow(1 - 2 * p(N / 2 + 1, N), M) / 2 
	total += pow(1 - 2 * p(N / 2 + 1, N), M) / 2 
print total

# Don't need to divide by 2 because we have contributions from squares on the other side as well.
total += float(N) / 2
print total
