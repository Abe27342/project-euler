import itertools
def f(mid5,a):
    if(a == len(mid5)-1):
        return([mid5[a],mid5[0]])
    return(mid5[a:a+2])

def isValid(perm):
    k = perm[0] + perm[5] + perm[6]
    #print(k)
    return(all([perm[i]+sum(f(perm[5:10],i)) == k for i in range(1,5)]))
def rot(p):
    first_half = p[0:5]
    second_half = p[5:10]
    first_half.append(first_half[0])
    first_half.remove(first_half[0])
    second_half.append(second_half[0])
    second_half.remove(second_half[0])
    return(first_half + second_half)

def orient(p):
    minimum = min(p[0:5])
    while(p[0] != minimum):
        p = rot(p)
    return(p)
 
def concat_set(p):
    p = orient(p)
    p = [str(i) for i in p]
    a = p[0]+p[5]+p[6]+p[1]+p[6]+p[7]+p[2]+p[7]+p[8]+p[3]+p[8]+p[9]+p[4]+p[9]+p[5]
    return(int(a))

valid_set = []
count = 0
for p in itertools.permutations(range(1,11)):
    count += 1
    if(count % 1000 == 0):
            print(count)
    if(10 in p[0:5]):
        if(isValid(list(p))):
            valid_set.append(list(p))
valid_set = [concat_set(p) for p in valid_set]
valid_set.sort(reverse=True)
print(valid_set[0])