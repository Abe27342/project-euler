import copy
from helpers import sieve
primes = sieve(30000)
#there's always a solution given for k by 2k = (k,2,1,1,1,1,...,1) so we only need to look in range(1,k+1)
table_of_vals = [30000 for i in range(12001)]
table_of_vals[0] = 0
table_of_vals[1] = 0

sum_list = [[] for i in range(24001)]

def multiply_set(n):
    if(n in primes):
        return([[n]])
    l = []
    for j in range(2,int(n**0.5)+1):
        if(n % j == 0):
            if(sum_list[int(n/j)] != []):
                a = copy.deepcopy(sum_list[int(n/j)])
            else:
                a = copy.deepcopy(multiply_set(int(n/j)))
            for i in a:
                i.append(j)
                i.sort()
                if(l.count(i) == 0):
                    l.append(i)
    l.append([n])
    sum_list[n] = l
    return(l)

def multiply_and_sum_set(n):
    x = copy.deepcopy(multiply_set(n))
    for i in x:
        for j in range(n-sum(i)):
            i.append(1)
        i.sort()
    return(x)


k = 12000
for i in range(2,2*k+1):
    x = multiply_and_sum_set(i)
    print(i)
    for j in x:
        if(len(j) < 12001):
            if(sum(j) < table_of_vals[len(j)]):
                table_of_vals[len(j)] = sum(j)
m = [table_of_vals[i] for i in range(k+1)]


print(m)
print(m.count(30000))
print(sum(set(m)))
'''
slow code but i guess it works

'''



