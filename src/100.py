'''
we assume that b+r = x and b-r = y. then it is possible to derive the following formulae.
'''
r = 3-8**0.5
s = 3+8**0.5

def x(n):
    return(0.25*((-1-2**0.5)*(r**n) + (2**0.5-1)*(s**n) + 2))
def y(n):
    return(int((2*x(n)**2 - 2*x(n) + 1)**0.5-x(n) + 1))
n = 1
while(x(n)<10**12):
    n += 1
print((x(n)+y(n))/2)