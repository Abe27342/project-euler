from numpy import matrix,around
from numpy.linalg import inv


#returns the vandermonde matrix on the set of alphas = 1-n
def get_vandermonde(n):
    v = []
    for i in range(n):
        v.append([])
        for j in range(n):
            v[i].append(int((i+1)**j))
    return(matrix(v))
        

#input a data_set of [(x1,f(x1)),(x2,f(x2),...,(xn,f(xn)] and take the first n points
def get_soln_vector(data_set,n):
    #get data to actually use
    d = matrix([[data_set[i][1]] for i in range(n)])
    return(inv(get_vandermonde(n))*d)

def calculate_f(soln_vector,n):
    ce = 0
    a = 0
    while(ce < len(soln_vector)):
        a += soln_vector[ce]*n**ce
        ce += 1
    a = around(a)
    a = int(a)
    return(a)
actual_degree = 10
#1-n+n**2-n**3+n**4-n**5+n**6-n**7+n**8-n**9+n**10
data = [(n,1-n+n**2-n**3+n**4-n**5+n**6-n**7+n**8-n**9+n**10) for n in range(1,12)]
print(data)

answer = 0
for i in range(1,actual_degree+1):
    print(calculate_f(get_soln_vector(data,i),i+1))
    answer += calculate_f(get_soln_vector(data,i),i+1)
print(answer)
