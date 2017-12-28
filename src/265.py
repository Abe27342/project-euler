
N = 5

def is_binary_circle(candidate):
	if candidate.count('0') != 2 ** (N - 1):
		return False
	tester = candidate + candidate[:N]
	seen_strings = set()
	for start in range(len(candidate)):
		if tester[start:start + N] in seen_strings:
			return False
		else:
			seen_strings.add(tester[start:start + N])
	return True

total = 0
# 2**N - N - 2 because we need some string of all 0s and then we also need ones on either side of this.
for num in range(1, 2**(2**N - N - 2)):
	cur_length = len(str(bin(num))) - 2
	required_length = 2**N - N - 2
	candidate = '0' * N + '1' + '0' * (required_length - cur_length) + str(bin(num))[2:] + '1'
	if is_binary_circle(candidate):
		print candidate
		total += int(candidate, 2)

print total