from decimal import Decimal
import math
phi = (Decimal(5).sqrt() + Decimal(1))/Decimal(2)

def frac(x):
    return(x-math.floor(x))

def is_pandigital(x):
    return({i for i in str(x)} == {'1','2','3','4','5','6','7','8','9'} and len(str(x)) == 9)


fl = [0,1,1,2,3,5]
def fibs(n):
    while n > len(fl):
        fl.append((fl[-1] + fl[-2])%1000000000)
    return fl[:n]

first_digit_list = [0,1,1,2,3,5]
def fibs2(n):
    count = 6
    while(first_digit_list[-1] + first_digit_list[-2] < 1000000000):
        first_digit_list.append(first_digit_list[-1]+first_digit_list[-2])
        count += 1
    for i in range(count, n):
        first_digit_list.append(round(round(10**(frac(i*math.log10(phi)-0.5*math.log10(5))),8)*10**8))
        #print('added %s as F_%s'%(first_digit_list[-1],i))
i = 2749
print(10**(frac(i*math.log10(phi)-0.5*math.log10(5))))
fibs(100000)
fibs2(100000)
l = []
a = []
for i in range(100000):
    if(is_pandigital(fl[i]) and is_pandigital(first_digit_list[i])):
        l.append(i)
    if(i == 2749):
        print(first_digit_list[i])
    if(is_pandigital(first_digit_list[i])):
        a.append(i)
print(l)
print(a)
