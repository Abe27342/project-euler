from math import factorial


def f(x):
    return(sum([factorial(int(i)) for i in str(x)]))

rep_list = [145,169,1454,871,872,45631,45632,363601]

def get_iterations(x):
    l = [x]
    while(l.count(l[-1]) == 1):
        x = f(x)
        l.append(x)
    return(len(l) - 1)

print(len([x for x in range(3,1000001) if get_iterations(x) == 60]))

def is_palindrome(n):
    if(n == ''):
        return(True)
    if(n[-1] == n[0]):
        return(True)
    else:
        return(False)