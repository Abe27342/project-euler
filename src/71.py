from fractions import Fraction
x = list({Fraction(3,7)-Fraction(int(3*i/7),i) for i in range(1,1000000)})
print('got list, now sorting')
x.sort()
print(x)


    