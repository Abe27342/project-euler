from decimal import Decimal, getcontext, Context

getcontext().prec = 50

total = Decimal(0)

for a in range(0, 100):
	total += Decimal(1) - getcontext().power(1 - getcontext().power(Decimal(2), -a), 32)
	print total
