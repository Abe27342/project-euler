from fractions import Fraction
from helpers import modinv

seq = [i for i in 'UDDDUdddDDUDDddDdDddDDUDDdUUDd']
seq.reverse()

x_coeff = Fraction(1)
const_coeff = Fraction(0)

while len(seq) > 0:
	next_elem = seq.pop()
	if next_elem == 'U':
		x_coeff *= Fraction(4, 3)
		const_coeff = const_coeff * Fraction(4, 3) + Fraction(2, 3)
	elif next_elem == 'd':
		x_coeff *= Fraction(2, 3)
		const_coeff = const_coeff * Fraction(2, 3) - Fraction(1, 3)
	else:
		x_coeff *= Fraction(1, 3)
		const_coeff *= Fraction(1, 3)


print x_coeff
print const_coeff

modulus = x_coeff.denominator
a = x_coeff.numerator
b = const_coeff.numerator

x = (-b) * modinv(a, modulus) % modulus
print modinv(a, modulus)
answer = x

while answer < 10 ** 15:
	answer += modulus

print answer