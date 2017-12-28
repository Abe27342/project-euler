from helpers import isPrimeMR, sieve


def digit_sum(n):
	return sum([int(i) for i in str(n)])

def right_truncatable_harshad_number(n):
	while n > 0:
		if n % digit_sum(n) == 0:
			n /= 10
		else:
			return False
	return True

n = 14
right_truncatable_harshad_nums = [[], [i for i in range(1, 10)], [i for i in range(10, 100) if right_truncatable_harshad_number(i)]]

i = 2
for i in range(2, n - 1):
	nums = []
	for right_truncatable_harshad_num in right_truncatable_harshad_nums[-1]:
		for last_digit in range(10):
			candidate = last_digit + 10 * right_truncatable_harshad_num
			if candidate % digit_sum(candidate) == 0:
				nums.append(candidate)


	right_truncatable_harshad_nums.append(nums)

total = 0
for j in range(1, n):
	strong_right_truncatable_harshad_nums = [i for i in right_truncatable_harshad_nums[j] if isPrimeMR(i / digit_sum(i))]
	
	for num in strong_right_truncatable_harshad_nums:
		for last_digit in range(10):
			candidate = last_digit + 10 * num
			if isPrimeMR(candidate):
				total += candidate

print total
