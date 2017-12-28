'''

S((p_m#)^n) = (n(n+1)/2)^m - n^m 

let x = (n+2)(n+1)/2 and y = n + 1

we want v_2(x^m - y^m) for m = 904961 and n ranging over a large number of things

according to LTE, we have

can show v_2 of this number is 0 unless n is 1 or 3 mod 4.


'''

def v_2(n):
	answer = 0
	while n % 2 == 0 and n > 0:
		n /= 2
		answer += 1
	return answer


# Q(n) is the total number of powers of 2
def Q(n):
	assert n % 4 == 0
	total = 0
	for k in range(n / 4):
		total += 904961 * v_2(2 * k + 2)
		total += v_2(2 * k)

	total += v_2(n / 2)

	return total

def highest_power_of_2_dividing_factorial(n):
	answer = 0
	while n > 0:
		answer += n / 2
		n /= 2
	return answer

def fast_Q(n):
	#total is sum from k = 1 to n / 4 of 904961 * (1 + v_2(k))
	# that's 904961 * (n / 4) + 904961 * (v_2(1) + v_2(2) + v_2(3) + ... + v_2(n / 4))
	answer = 904961 * (n / 4)
	answer += 904961 * highest_power_of_2_dividing_factorial(n / 4)
	# and then also sum from k = 1 to n / 4 - 1 of v_2(2 * k)
	# which is n / 4 + (v_2(1) + ... + v_2(n / 4 - 1))
	answer += n / 4 + highest_power_of_2_dividing_factorial(n / 4 - 1)
	answer += v_2(n / 4)
	return answer

print [(4 * i, Q(4 * i) - fast_Q(4 * i)) for i in range(1, 100) if Q(4 * i) != fast_Q(4 * i)]
print fast_Q(10**12)