
def tri(n):
	if n == 0:
		return '0'
	L = []
	while n > 0:
		L.append(str(n % 3))
		n = n / 3
	L.reverse()
	return ''.join(L)

def nth_num_brute_force(n):
	coeffs = [int(i) for i in tri(n)]
	num = reduce(lambda a,b : 10 * a + b, coeffs)
	return num

N = 10000


print [nth_num_brute_force(i)  for i in range(10)]

answer = 1
for n in range(2, N + 1):
	i = 1
	while (nth_num_brute_force(i) % n) != 0:
		#print nth_num_brute_force(i)
		i += 1
	answer += nth_num_brute_force(i) / n
	print n
	print answer

print answer 



# Code above doesn't quite get there cuz 9999 brute force is too hard.
# It gets this
# 9997
# 648538002946
# 9998
# 648549117390


# From there, we can brute force 9999 and 10000. 10000 contributes 1 to the sum, and 9999 contributes
# 11112222222222222222 / 9999

# thus the answer is 1111981904675169.
