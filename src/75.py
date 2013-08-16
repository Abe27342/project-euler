from helpers import gcd

lim = 1500001


def get_p(m,n):
    return(2*m*(m+n))

l = [0 for i in range(lim)]
    

for m in range(2000):
    n = 1
    while(n < m and get_p(m,n) < lim):
        if(gcd(m,n) == 1 and m%2 != n%2):
            f = 1
            while(f*get_p(m,n) < lim):
                #print(f,m,n)
                l[f*get_p(m,n)] += 1
                f += 1
        n += 1
        
count = 0
for i in l:
    if(i == 1):
        count += 1
#print(l)
print(count)