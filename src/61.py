import itertools

def f3(n):
    return(int(n*(n+1)/2))
def f4(n):
    return(n**2)
def f5(n):
    return(int(n*(3*n-1)/2))
def f6(n):
    return(n*(2*n-1))
def f7(n):
    return(int(n*(5*n-3)/2))
def f8(n):
    return(n*(3*n-2))

s3 = [str(f3(i)) for i in range(200) if 999 < f3(i) < 10000]
s4 = [str(f4(i)) for i in range(200) if 999 < f4(i) < 10000]
s5 = [str(f5(i)) for i in range(200) if 999 < f5(i) < 10000]
s6 = [str(f6(i)) for i in range(200) if 999 < f6(i) < 10000]
s7 = [str(f7(i)) for i in range(200) if 999 < f7(i) < 10000]
s8 = [str(f8(i)) for i in range(200) if 999 < f8(i) < 10000]

def check(n):
    return([n in s3,n in s4, n in s5, n in s6, n in s7, n in s8])

def covers_all_sets(a,b,c,d,e,f):
    x = [check(a),check(b),check(c),check(d),check(e),check(f)]
    y = [i for i in zip(*x)]
    for i in range(6):
        if((i != 0 and i != 3 and y[i].count(True) > 1) or y[i].count(True) == 0):
            return(False)
    return(True)

count = 0
for s0,s1,s2 in itertools.permutations([s3,s4,s5,s6,s7,s8],3):
    count += 1
    #print('try set #: ',count)
    o = [s3,s4,s5,s6,s7,s8]
            
    #print(opposite[0][-1],opposite[1][-1],opposite[2][-1],opposite[5][-1])
    o.remove(s0)
    o.remove(s1)
    o.remove(s2)
    opposite = []
    for i in range(3):
        for j in range(len(o[i])):
            opposite.append(o[i][j])
            
    for i in s0:
        for j in s1:
            if((i+j)[2:6] in opposite):
                for k in s2:
                    if((j+k)[2:6] in opposite and (k+i)[2:6] in opposite):
                        a = (i+j)[2:6]
                        b = (j+k)[2:6]
                        c = (k+i)[2:6]
                        if(covers_all_sets(a,b,c,i,j,k)):
                            print('answer = ',(int(a)+int(b)+int(c)+int(i)+int(j)+int(k)))
                            break

    
    