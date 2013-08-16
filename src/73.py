from helpers import gcd
count = 0
for d in range(1,12001):
    n = int(d/3)+1
    while n < d/2:
        print(d,n)
        if(gcd(n,d) == 1):
            count += 1
        n += 1
print(count)
