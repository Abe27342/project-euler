
class change_counter:
    def __init__(self):
        self.l = []
    
    
    def _f(self,s,n,m):

        if(n < 0):
            return(0)
        if(m <= 0 and n > 0):
            return(0)
        
        #print('n,m == ',n,m)
        return(self.l[n][m])
    def partitions(self,n):
        return(self.make_change(range(1,n+1),n))
    def partitions_list(self,n):
        self.make_change(range(1,n+1),n)
        return(self.l)
    def make_change(self,s,n):
        return(self._make_change(s,n,len(s)))

    def _make_change(self,s,n,m):
        self.l = [[1]]
        #l[i][j] will contain make_change(i,j)
        #make_change(i,j) should be the number of ways to make change for i using the first j elements of set s... so that's s[0],s[1],...,s[j-1]
        for i in range(1,n+1):
            #these are make_change(1,0), make_change(2,0), ..., make(change(n,0)
            self.l.append([0])
        
        for i_n in range(n+1):
            for i_m in range(1,m+1):
                #print('i_n,i_m == ',i_n,i_m)
                self.l[i_n].append(self.__f(s, i_n, i_m-1) + self.__f(s, i_n-s[i_m-1],i_m))
        #print(self.l)
        return(self.l[-1][-1])
    
    
    def modified_make_change(self,s,n,m):
        self.l = [[1]]
        #l[i][j] will contain make_change(i,j)
        #make_change(i,j) should be the number of ways to make change for i using the first j elements of set s... so that's s[0],s[1],...,s[j-1]
        i_n = 0
        while(self.l[-1][-1] != 0):
            if(i_n != 0):
                self.l.append([0])
            for i_m in range(1,m+1):
                #print('i_n,i_m == ',i_n,i_m)
                self.l[i_n].append((self.__f(s, i_n, i_m-1) + self.__f(s, i_n-s[i_m-1],i_m)) % 1000000)
            i_n += 1
            print(i_n)
        i_n -= 1
        print('answer = ',i_n)
        #print(self.l)
        return(self.l[-1][-1])
c = change_counter()
#c.modified_make_change(range(1,10001), 10000, 10000)
'''
the following will solve problem 77:
from helpers import sieve
primes = sieve(600)
for x in range(1,601):
    if(c.make_change(primes,x) > 5000):
        print('answer = ',x)
        break
    print(x)
'''

'''
x = c.partitions_list(30000)
y = [i for i in range(30001) if(x[i][i] % 1000000 == 0)]
print(y)
'''
    