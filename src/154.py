'''

Coeffs in this expansion are

200000! / (a! b! c!) where a + b + c = 200000.
'''
def from_base_10(n, new_base):
	answer = []
	while n > 0:
		answer.append(n % new_base)
		n /= new_base
	answer = reversed(answer)
	return [i for i in answer]


def num_powers_of_k_in_n_factorial(k, n):
	answer = 0
	while n > 0:
		answer += n / k
		n /= k 
	return answer

two_powers = [i - num_powers_of_k_in_n_factorial(2, i) for i in range(200001)]
five_powers = [float(i) / 4 - num_powers_of_k_in_n_factorial(5, i) for i in range(200001)]


# The sum of the elements in five_powers has to be at least 14
# and the sum of the elements in two_powers has to be at least 18.
print min(two_powers), max(two_powers), min(five_powers), max(five_powers)
print len([i for i in range(200001) if two_powers[i] >= 6 and five_powers[i] >= 4.5])
print len([from_base_10(i, 5) for i in range(200001) if five_powers[i] >= 4.5])
print num_powers_of_k_in_n_factorial(5, 200000), num_powers_of_k_in_n_factorial(2, 200000)