
l = [0 for i in range(10000001)]
def f(n):
    return(sum([int(i)**2 for i in str(n)]))

def get_ending(x):
    n = x
    print(x)
    while(n != 1 and n != 89):
        n = f(n)
        if(l[n] != 0):
            l[x] = l[n]
            return(l[n])
    l[x] = n
    return(n)


print(len([x for x in range(1,10000001) if get_ending(x) == 89]))