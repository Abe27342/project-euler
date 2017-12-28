

def best_k_part_partition(n, k):
	a = (n - k * (k - 1) / 2) / k
	extra = n - k * a - (k * (k - 1)) / 2
	initial_list = [a + i for i in range(k)]
	for i in range(1, extra + 1):
		initial_list[-i] += 1
	return initial_list

def f(n):
	k = 1
	max_value = n
	k_for_max_value = 1
	while best_k_part_partition(n, k)[0] > 0:
		candidate = best_k_part_partition(n, k)
		product = reduce(lambda a, b : a * b, candidate)
		if product > max_value:
			max_value = product
			k_for_max_value = k
		k += 1
	return (max_value, k_for_max_value)

'''
These lines suggest that the first time for which m(n) = k is k * (k + 3) / 2.

print [(i, f(i)[1]) for i in range(1, 101) if f(i)[1] != f(i-1)[1]]
print [(k, k * (k + 3) / 2) for k in range(1, 10)]

Then we can sum m(n) * f(n) over all n for which m(n) = k by summing f(n) over
range(k * (k + 3) / 2, (k + 1) * (k + 4) / 2) and multiplying by 4.

'''

'''

This function suggests that for a given value of k, the first max partition for that value is 
[2, 3, 4, ..., k + 1].
These partitions increase up to [3, 4, ..., k + 2], and there is one last one with a value 
[3, 4, ..., k + 1, k + 3].

The sum of the first k + 1 partitions is then k * (2 + 3 + ... + k + 2)
= k * ((k + 2)(k + 3)/2 - 1)
and the sum over the last partition is 
 k + 1 + (k + 1)(k + 2) / 2 - 3
'''
def slow_f_sum_over_mn_equalling_k(k):
	return sum([reduce(lambda a, b : a * b, best_k_part_partition(n, f(n)[1])) for n in range(k * (k + 3) / 2, (k + 1) * (k + 4) / 2)])

def f_sum_over_mn_equalling_k(k):
	total = k * ((k + 2)*(k+3)/2 - 1)
	total += k - 2 + (k + 1) * (k + 2) / 2
	return total

from helpers import modinv
from math import sqrt

limit = 10**14

modulus = 982451653
# print  1683550844462 % modulus

max_k = int(sqrt(2 * limit))
while (max_k + 1) * (max_k + 4) / 2 > limit:
	max_k -= 1

remainder = limit - (max_k + 1) * (max_k + 4) / 2

print max_k, remainder
total = 1
current_inverse_sum = modinv(2, modulus)
modinv2 = modinv(2, modulus)
current_product = 2
for k in range(1, max_k + 1):
	if k % 10**6 == 0:
		print k
	current_product *= (k + 2)
	current_product %= modulus
	modinvk2 = modinv(k + 2, modulus)
	current_inverse_sum += modinvk2
	current_inverse_sum %= modulus

	# Current product now contains 2 * 3 * ... * (k + 2).
	# Current inverse sum now contains (1/2 + 1/3 + ... + 1/(k+2))
	total += k * current_inverse_sum * current_product
	# Also need to add the 3, 4, 5, ..., k + 1, k + 3 partition.
	total += k * current_product * (k + 3) * modinvk2 * modinv2
	total %= modulus


# current product contains 2 * 3 * ... * (max_k + 2).
current_product *= max_k + 3
for j in range(max_k + 3, max_k + 3 - remainder - 1, -1):
	# Now with the remaining ones, we need to add 
	# current product over the remaining largest numbers.
	total += (max_k + 1) * current_product * modinv(j, modulus)
	total %= modulus

print total

# print [best_k_part_partition(n, f(n)[1]) for n in range(k * (k + 3) / 2, (k + 1) * (k + 4) / 2)]
# print sum([f(i)[0] * f(i)[1] for i in range(1, (max_k + 1) * (max_k + 4) / 2 + 1)]) % modulus
# print sum([f(i)[0] * f(i)[1] for i in range(1, limit + 1)]) % modulus
