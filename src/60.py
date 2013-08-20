import itertools
from helpers import sieve, isPrime

primes = sieve(10000)
print("primes generated")


def concat(a,b):
    return(int(str(a) + str(b)))
def f(a,b):
    return(isPrime(concat(a,b)) and isPrime(concat(b,a)))
def check_concat(a,b,c,d,e):
    return(f(a,b) and f(a,c) and f(a,d) and f(a,e) and f(b,c) and f(b,d) and f(b,e) and f(c,d) and f(c,e) and f(d,e))

for p1 in primes:
    print(p1)
    for p2 in primes:
        if(p2 < p1):
            continue
        if(f(p1,p2)):
            print(p1,p2)
            for p3 in primes:
                if(p3 < p2):
                    continue
                if(f(p1,p3) and f(p2,p3)):
                    for p4 in primes:
                        if(p4 < p3):
                            continue
                        if(f(p1,p4) and f(p2,p4) and f(p3,p4)):
                            for p5 in primes:
                                if(p5 < p4):
                                    continue
                                if(f(p1,p5) and f(p2,p5) and f(p3,p5) and f(p4,p5)):
                                    print('answer: ',p1,p2,p3,p4,p5)

