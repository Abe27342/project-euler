from helpers import sieve
import itertools
num_set = ['0','1','2','3','4','5','6','7','8','9','*']
primes = sieve(100000000)
print('primes generated')

def checkPrimeFamily(n):
    count = 0
    m = [i for i in n]
    for i in range(10):
        for x in range(len(n)):
            if(n[x] == '*'):
                m[x] = str(i)
        if(int(''.join(m)) in primes):
            count += 1
    if(count > 7):
        print(n)


for raw_num_list in itertools.product(num_set,repeat=7):
    raw_num_list = [i for i in raw_num_list]
    if(raw_num_list.count('*') == 3):
        for i in ['1','3','7','9']:
            raw_num_list.append(i)
            checkPrimeFamily(raw_num_list)

'''
def triple_digit(n):
    n = str(n)[0:-1]
    x = [n.count(i) for i in n]
    if(3 in x):
        indices = [i for i in range(len(x)) if x[i] == 3]
        return(indices)


#print(triple_digit(3221125))

m = [p for p in primes if triple_digit(p) != None]
m.sort(key=lambda x:triple_digit(x))
print('first stage done')
#print(m)

paired_m = []
i = 0
while(i < len(m)):
    p = m[i]
    count = 0
    while(i+count < len(m) and triple_digit(p) == triple_digit(m[i+count])):
        count += 1
    #print(triple_digit(p),triple_digit(p+count))
    paired_m.append([m[j] for j in range(i,i+count)])
    i += count
#print(paired_m)
print('second stage done')

for triple_list in paired_m:
    if(len(triple_list) == 1):
        print(triple_list)
    for i in range(len(triple_list)):
        element = triple_list[i] #i could use enumerate but it's 1am gg
        indices = triple_digit(element)
        element = list(str(element))
        for c in indices:
            element[c] = '*'
        triple_list[i] = ''.join(element)
    #print(triple_list)
    for s in triple_list:
        if(triple_list.count(s) == 8):
            print(s)
            break
        else:
            triple_list.remove(s)
'''   
            
            

