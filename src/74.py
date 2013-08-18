from math import factorial


def f(x):
    return(sum([factorial(int(i)) for i in str(x)]))

def get_iterations(x):
    l = [x]
    while(l.count(l[-1]) == 1):
        x = f(x)
        l.append(x)
    return(len(l) - 1)

print(len([x for x in range(3,1000001) if get_iterations(x) == 60]))
