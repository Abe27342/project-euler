partitions = [1]

def p(n):
    return(int(n*(3*n-1)/2))


def gen(n):
    x = 1
    while(p(x) <= n):
        if(x > 0):
            yield [p(x),int((-1)**(x-1))]
            x = -x
        else:
            yield [p(x),int((-1)**(x-1))]
            x = -x + 1
    
    
for i in gen(7):
    print(i)
#returns the first number n such that the number of partitions of n is divisible by a
def calc_partitions(a):
    i = 1
    while(partitions[-1] != 0):
        running_tot = 0
        for x,y in gen(i):
            #print('i,x == ',i,x)
            running_tot += y*partitions[i-x]
        partitions.append(running_tot % a)
        i += 1
    i -= 1
    return(i)
    print(i)
        

print(calc_partitions(1000000))
#print(partitions)
