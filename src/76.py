
s = range(1,3)
def make_change(n,m):
    if(n == 0):
        return(1)
    if(n < 0):
        return(0)
    if(m <= 0 and n > 0):
        return(0)
    
    return(make_change(n,m-1) + make_change(n-s[m],m))
    
    
    
print(make_change(4,1))


#returns the number of ways to make change for n with the set s
def dyn_make_change(s,n,m):
    l = []
    #l[i][j] will contain make_change(i,j)
    for i in range(n):
        l.append([0])
    