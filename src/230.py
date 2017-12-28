

A = '1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679'
B = '8214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196'


lengths = [len(A), len(B)]
upper_limit = (127 + 19 * 17) * pow(7, 17) + 100

while lengths[-1] < upper_limit:
	lengths.append(lengths[-1] + lengths[-2])

def nth_digit_of_kth_number(n, k):
	if k == 0:
		return A[n - 1]
	elif k == 1:
		return B[n - 1]
	else:
		second_trailing_length = lengths[k - 2]
		trailing_length = lengths[k - 1]
		if n <= second_trailing_length:
			return nth_digit_of_kth_number(n, k - 2)
		else:
			return nth_digit_of_kth_number(n - second_trailing_length, k - 1)


def D(n):
	k = 0
	while lengths[k] < n:
		k += 1
	return nth_digit_of_kth_number(n, k)



total = 0
for i in range(18):
	total += pow(10, i) * int(D((127 + 19 * i) * pow(7, i)))

print total