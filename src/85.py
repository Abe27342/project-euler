'''

for an nxm rectangle, there are 
((((n+1)*(m+1)) choose 2) - (n+1)*(m+1 choose 2) - (m+1)(n+1 choose 2))/2
rectangles. Simplifying,

'''
import itertools

def choose_2(x):
    return(int(x*(x-1)/2))

def f(m,n):
    return(int((choose_2((n+1)*(m+1))-(n+1)*choose_2(m+1)-(m+1)*choose_2(n+1))/2))

x = set([(m,n) for m,n in itertools.product(range(100), repeat=2) if 1999997 < f(m,n) < 2000001])
x = list(x)
x.sort()
print(x)