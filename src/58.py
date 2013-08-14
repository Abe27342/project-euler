from helpers import isPrime
'''
square of length 2n+1
there are 4n+1 elements
n are given by n^2 from 1 to n
n are given by 4n^2-2n+1 from 1 to n
n are given by 4n^2 + 1 from 1 to n
n are given by 4n^2 + 2x + 1 from 1 to n 

'''

count = 8
size = 9
n = 4
print (count + 0.0)/(4*n+1)
while((count + 0.0)/(4*n+1) > 0.1):
    if isPrime(4*n**2 - 2*n + 1):
        count += 1
    if isPrime(4*n**2 + 1):
        count += 1
    if isPrime(4*n**2 + 2*n + 1):
        count += 1
    print count,size
    
    
    size += 2
    n += 1
print size