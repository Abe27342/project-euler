
'''
from helpers import sieve
primes = sieve(10000000)
count = 0
for i in range(len(primes)-5):
    if((primes[i]-1)**0.5 == int((primes[i]-1)**0.5)):
        if(primes[i+1] == primes[i]+2 and primes[i+2] == primes[i]+6 and primes[i+3] == primes[i] + 8 and primes[i+4] == primes[i] + 12 and primes[i+5] == primes[i] + 26):
            count += int((primes[i] - 1)**0.5)
            
print(count)

'''
'''
oops i misread the problem... darn
'''
x = '314159265358979323846264338327950288'
x = x.replace('1','C')
x = x.replace('2','D')
x = x.replace('3','E')
x = x.replace('4','F')
x = x.replace('5','G')
x = x.replace('6','A')
x = x.replace('7','B')

print(x)        