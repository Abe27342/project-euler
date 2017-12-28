# Plugging the thing into mathematica, we have
# f_n(x,y,z) = (x + y + z)(x^n + y^n - z^n)
# lelelelleleelellellelelellee
# so n = -2, -1, 0, 1, or 2 by Fermat's Last Theorem. Also 0 impossible.
# Condition that 0 < x,y,z < 1 means we can alternatively let n = 1 or 2
# and take x,y,z to be whatever rational numbers with numerators and denominators
# less than 35.
# Answer is 12519 for 10.
from itertools import product, combinations
from fractions import Fraction

order = 35
s_used = set()

squares_table = {i**2 : i for i in range(1, order + 1)}

# Returns sqrt(x^2 + y^2), but as a fraction and accurately.
# If x^2 + y^2 not a perfect square, returns 1 / 1 in order to short circuit.
def L2Norm(x,y):
    z2 = x*x + y*y
    if z2.denominator not in squares_table or z2.numerator not in squares_table:
        return Fraction(order, order)
    return Fraction(squares_table[z2.numerator], squares_table[z2.denominator])

def maybe_add(x,y,z):
    if (z.numerator < z.denominator <= order):
        s_used.add(x + y + z)


for ((a,b),(c,d)) in product(combinations(range(1, order + 1), 2), repeat = 2):
    x = Fraction(a, b)
    y = Fraction(c, d)
    if x > y:
        continue
    z = x + y
    maybe_add(x,y,z)
    z = 1/(1/x + 1/y)
    maybe_add(x,y,z)
    z = L2Norm(x,y)
    maybe_add(x,y,z)
    z = 1/L2Norm(1/x,1/y)
    maybe_add(x,y,z)

t = sum(s_used)
print t
print t.numerator + t.denominator
