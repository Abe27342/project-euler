import itertools



def is_possible(n, s1, s2):
    d1 = n//10
    d2 = n % 10
    if(6 in s1 or 9 in s1):
        s1 = s1.union({6,9})
    if(6 in s2 or 9 in s2):
        s2 = s2.union({6,9})
    
    if((d1 in s2 and d2 in s1) or (d1 in s1 and d2 in s2)):
        return(True)
    return(False)

count = 0
for s1,s2 in itertools.product(itertools.combinations(range(10),6),repeat=2):
    if(all([is_possible(i**2,set(s1),set(s2)) for i in range(1,10)])):
        count += 1
print(count/2)