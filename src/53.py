import math
def ncr(n, k):
    return(math.factorial(n)/(math.factorial(k)*math.factorial(n-k)))
print(ncr(100,50))

print(sum([len([ncr(n,k) for k in range(n) if ncr(n,k) > 1000000]) for n in range(101)]))