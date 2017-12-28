from expr_helpers import Num, Exp 
from helpers import crt

a00 = 1
a11 = 3
a22 = 7
a33 = 2**6 - 3
a44 = Exp(Num(2), Exp(Num(2), Exp(Num(2), Exp(Num(2), Num(16))))).compute_value(7**8)
a44 = crt([(a44 - 3, 7**8), (-3, 2**8)])


expr = Exp(Num(2), Num(2))
last_value = 0
i = 0
while expr.compute_value(7**8) != last_value:
	last_value = expr.compute_value(7**8)
	expr = Exp(Num(2), expr)
	i += 1
	print i

print expr.compute_value(7**8)
expr = Exp(Num(2), expr)
print expr.compute_value(7**8)
stabilized = expr.compute_value(7**8)
a55 = a66 = crt([(stabilized - 3, 7**8), (-3, 2**8)])

total = a00 + a11 + a22 + a33 + a44 + a55 + a66
total %= 14**8
print total