

def get_area(a,b,c):
    s = (a+b+c)/2
    return((s*(s-a)*(s-b)*(s-c))**0.5)
print(get_area(5,5,6))

x = [(n,(n-1)/2,(n**2-((n-1)/2)**2)**0.5) for n in range(2,100000) if get_area(n,n,n-1) == int(get_area(n,n,n-1))]
y = [(n,(n+1)/2,(n**2-((n+1)/2)**2)**0.5) for n in range(2,100000) if get_area(n,n,n+1) == int(get_area(n,n,n+1))]
a = []
b = []
#m^2+n^2,m^2-n^2,2mn
for triple in y:
    a.append((((triple[0]+triple[1])/2)**0.5,((triple[0]-triple[1])/2)**0.5))
for triple in x:
    b.append((((triple[0]+triple[2])/2)**0.5,((triple[0]-triple[2])/2)**0.5))
print(y)
print(a)
print(x)
print(b)

#that code motivates the following formulae for (m,n) and generating pythagorean triples:

#r = 2+3**0.5
#s = 2-3**0.5
#a = 3+2*3**0.5
#b = 3-2*3**0.5

'''
y is the set of triangles that are (n,n,n+1). To find perimeter, we just need 4m^2, where m is given by get_generating_val_2(n) for 0 <= n.
x is the set of triangles that are (n,n,n-1). To find perimeter, we need 2*(m^2 - n^2 + 2mn), where they're


'''

#a valid generator is get_generating_val_1(n+1),get_generating_val_1(n)
def g1(n):
    r = 2+3**0.5
    s = 2-3**0.5
    a = 3+2*3**0.5
    b = 3-2*3**0.5
    return(round(1/6 * (a*r**n + b*s**n)))

#a valid generator triple that will give (m^2-n^2,2mn,m^2+n^2) is given by get_generating_val_2(n),get_generating_val_1(n)
def get_generating_val_2(n):
    r = 2+3**0.5
    s = 2-3**0.5
    return(round(1/2 * (r**(n+1) + s**(n+1))))
print(g1(1))
print(get_generating_val_2(0))
p1 = [4*get_generating_val_2(n)**2 for n in range(20) if 4*get_generating_val_2(n)**2 < 1000000000]
p2 = [2*(g1(n+1)**2+g1(n)**2+2*g1(n+1)*g1(n)) for n in range(20) if 2*(g1(n+1)**2+g1(n)**2+2*g1(n+1)*g1(n)) < 1000000000]
print(sum(p1) + sum(p2))

