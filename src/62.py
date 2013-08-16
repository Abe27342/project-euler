def get_digit_list(n):
    l = []
    for i in str(n):
        if(l.count([i,str(n).count(i)]) == 0):
            l.append([i,str(n).count(i)])
    l.sort()
    return(l)

x = [get_digit_list(i**3) for i in range(10000)]
'''
for i in x:
    if(x.count(i) == 5):
        print(i)
'''
for i in range(10000):
    if(get_digit_list(i**3) == [['0', 1], ['1', 1], ['2', 1], ['3', 2], ['4', 1], ['5', 2], ['6', 1], ['7', 1], ['8', 1], ['9', 1]]):
        print(i**3)        
        
