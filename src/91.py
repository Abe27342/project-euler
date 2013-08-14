import itertools
from fractions import Fraction
def perpendicular(x1,y1,x2,y2,x3,y3):
    perp = [False,False,False]
    try:
        perp[0] = slope(x1,y1,x2,y2) * slope(x1,y1,x3,y3) == -1
    except ZeroDivisionError:
        pass
    try:
        perp[1] = slope(x1,y1,x2,y2) * slope(x2,y2,x3,y3) == -1
    except ZeroDivisionError:
        pass
    try:
        perp[2] = slope(x1,y1,x3,y3) * slope(x2,y2,x3,y3) == -1
    except ZeroDivisionError:
        pass
    return(any(perp))
def slope(x1,y1,x2,y2):
    return(Fraction(y2-y1,x2-x1))
print(perpendicular(0,0,1,0,1,0))


def num_of_triangles(n):
    count = 0
    for ((x1,y1),(x2,y2)) in itertools.combinations(itertools.product(range(n+1), repeat=2),2):
        if(not((x1 == x2 and y1 == y2) or (x1 == 0 and y1 == 0) or (x2 == 0 and y2 == 0))):
    
            if((x1 == 0 and y2 == 0) or (x2 == 0 and y1 == 0) or (x1 == 0 and y1 == y2) or (x2 == 0 and y1 == y2) or (y1 == 0 and x1 == x2) or (y2 == 0 and x1 == x2)):
                #print(x1,y1,x2,y2)
                count += 1
    
            elif(perpendicular(x1,y1,x2,y2,0,0)):
                #print(x1,y1,x2,y2)
                count += 1
    return(count)

#x = [num_of_triangles(i) for i in range(15)]
#print(x)
print(num_of_triangles(50))
