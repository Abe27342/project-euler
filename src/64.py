
#sqrt(n) = floor(sqrt(n)) + sqrt(n)-floor(sqrt(n))
#a1 = floor(sqrt(n))
#num_part_1 = 1
#num_part_2 = l[-1]
#den = 1
from helpers import gcd
'''
then it goes to
den/(n**0.5 + num_part_2)
= l.append(int(den*(n**0.5+num_part_2)/(n-num_part_2**2)))

den*(n**0.5+num_part_2)/(n-num_part_2**2) - l[-1] 

den,num_part_1,num_part_2 = n-num_part_2**2,den,-den * num_part_2
num_part_2 -= den*l[-1]
(num_part_1*n**0.5 + num_part_2)/den - l[-1] = num_part_1 * 



'''
def abs(x):
    if(x < 0):
        return(-x)
    return(x)
#(num_part_1 * n**0.5 + num_part_2)/den
#
def get_periodic_fraction(n):
    l = []
    num_part_1 = 1
    num_part_2 = -int(n**0.5)
    den = 1
    l.append([int(n**0.5),den,num_part_1,num_part_2])
    while(l.count(l[-1]) == 1):
        den,num_part_1,num_part_2 = num_part_1**2*n-num_part_2**2,num_part_1*den,-den*num_part_2
        l.append([int((num_part_1*n**0.5+num_part_2)/den),den,num_part_1,num_part_2])
        #print(l)
        num_part_2 -= den*l[-1][0]
        d = gcd(gcd(abs(den),abs(num_part_1)),gcd(abs(den),abs(num_part_2)))
        den,num_part_1,num_part_2 = int(den/d),int(num_part_1/d),int(num_part_2/d)
        #print(den,num_part_1,num_part_2)
    x = [l[i][0] for i in range(len(l)-1)]
    return(x)
    
print(get_periodic_fraction(23))
m = [1 for i in range(2,10001) if i**0.5 != int(i**0.5) and len(get_periodic_fraction(i)) % 2 == 0]
print(sum(m))
