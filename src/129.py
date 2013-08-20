from helpers import gcd
from helpers import sieve
primes = sieve(100000)

#answer is the first number n such that ord_{9n}(10) is >1000000

def o(n):
    answer = 1
    while(pow(10,answer,9*n) != 1):
        answer += 1
    return(answer)
done = False
count = 3
answer_count = 0
print(o(91))
l = []
while(not done):
    if(gcd(10,count) == 1 and count % o(count) == 1 and count not in primes):
        print('answer #%s = %s'%(answer_count+1,count))
        answer_count += 1
        l.append(count)
        if(answer_count == 25):
            print('done')
            break
    count += 1
    
    
print('final answer:',sum(l))