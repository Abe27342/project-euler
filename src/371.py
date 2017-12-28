from decimal import *
from helpers import memoize

getcontext().prec = 30



@memoize
def B(i, k):
	if i == 1:
		if k == 1:
			return Decimal(998) / Decimal(1000)
		if k == 0:
			return Decimal(1) / Decimal(1000)
		else:
			return 0
	return Decimal(k + 1) / Decimal(1000) * B(i - 1, k) + Decimal(998 - 2 * (k - 1)) / Decimal(1000) * B(i - 1, k - 1)
	
@memoize
def C(i, k):
	if i == 1:
		if k == 0:
			return Decimal(1) / Decimal(1000)
		else:
			return 0
	return Decimal(1) / Decimal(1000) * B(i - 1, k) + Decimal(k + 1) / Decimal(1000) * C(i - 1, k) + Decimal(998 - 2 * (k - 1)) / Decimal(1000) * C(i - 1, k - 1)


def A(i):
	answer = 0
	for k in range(500):
		answer += B(i, k)
		answer += C(i, k)
	return answer


print A(2)

i = 1
# Need to add 1 :^)^)^)^^)^)^))^^^)^)^))^)^^))^)^)^ FUCK
running_total = 1
while False:
	running_total += A(i)
	i += 1
	print i, running_total