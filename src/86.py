import itertools
from helpers import gcd

'''
def g(a,b,c):
    return(c**2+(a+b)**2)
    #return(min([a**2+(b+c)**2,b**2+(a+c)**2,c**2+(a+b)**2]))
def y(a,b):
    c = int((a**2+b**2)**0.5)
    if(a % 2 == 0):
        a,b = b,a
    return([int(((a+c)/2)**0.5),int(((c-a)/2)**0.5)])

 
triple_set = []
def isValid(a,b,c):
    x = g(a,b,c)
    return(x**0.5 == int(x**0.5))

count = 0
for a,b,c in itertools.combinations_with_replacement(range(1,101),3):
    if(isValid(a,b,c)):
        if(triple_set.count(y(c/gcd(c,a+b),(a+b)/gcd(c,a+b))) == 0):
            triple_set.append(y((a+b)/gcd(c,a+b),c/gcd(c,a+b)))
        #print(c,a+b,(c**2+a**2+2*a*b+b**2)**0.5)
        count += 1
print(count)
print(triple_set)
print(len(triple_set))
'''
#idea: take the pythagorean triple (m^2-n^2,2mn,m^2+n^2) and set (m^2-n^2,2mn) = (c,b+a)
lim = 1818
def f(a,b):
    #first find all triangles that partition a. then (i,a-i) must satisfy i < a, i < b+1, i <= lim, a-i < b+1, a-i <= lim
    #so minimal i will satisfy i >= a-b, i >= a-lim
    #maximal i will satisfy i <= a-1, i <= b, i <= lim
    count = 0
    if(b <= lim):
        min_i = max([a-b,a-lim,1])
        max_i = min([a-1,b,lim])
        #print(min_i,max_i)
        if((max_i-min_i+2)//2 > 0):
            count += (max_i-min_i + 2)//2
    if(a <= lim):
        min_i = max([b-a,b-lim,1])
        max_i = min([b-1,a,lim])
        #print(min_i,max_i)
        if((max_i-min_i+2)//2 > 0):
            count += (max_i-min_i + 2)//2
    if(count < 0):
        return(0)
    return(count)

    
    


def get_num_of_cuboids(m,n,k):
    a = k*(m**2-n**2)
    b = 2*k*m*n
    if(a > 2*lim or b > 2*lim):
        return(0)
    return(f(a,b))
print(get_num_of_cuboids(10,1,1))

print(get_num_of_cuboids(2,1,26))       
m = 2
n = 1
count = 0
while(m < 500):
    while(n < m):
        if(gcd(m,n) == 1):
            #if(get_num_of_cuboids(m,n,1) > 0):
                #print(m,n)
            k = 1
            while(get_num_of_cuboids(m,n,k) > 0):
                #print('get_num_of_cuboids(%s,%s,%s)=%s'%(m,n,k,get_num_of_cuboids(m,n,k)))
                
                count += get_num_of_cuboids(m,n,k)
                k += 1
        n += 2
        
    m += 1
    if(m % 2 == 0):
        n = 1
    else:
        n = 2
print('broke out of loop, m,n ==',m,n)
print(count)