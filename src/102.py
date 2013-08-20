
def distance(x1,x2,y1,y2):
    return(((x1-x2)**2+(y1-y2)**2)**0.5)

def area(x1,y1,x2,y2,x3,y3):
    a = distance(x1,x2,y1,y2)
    b = distance(x1,x3,y1,y3)
    c = distance(x2,x3,y2,y3)
    s = (a+b+c)/2
    return((s*(s-a)*(s-b)*(s-c))**0.5)

def contains_origin(co_ords):
    x1 = co_ords[0]
    y1 = co_ords[1]
    x2 = co_ords[2]
    y2 = co_ords[3]
    x3 = co_ords[4]
    y3 = co_ords[5]
    a1 = area(x1,y1,x2,y2,x3,y3)
    b1 = area(x1,y1,x2,y2,0,0)
    b2 = area(x1,y1,x3,y3,0,0)
    b3 = area(x2,y2,x3,y3,0,0)
    if(round(a1,5) == round((b1+b2+b3),5)):
        return(True)
    else:
        return(False)

x = open('102triangles.txt').readlines()
y = [eval('[' + x[i] + ']') for i in range(len(x))]

count = 0
for i in y:
    if(contains_origin(i)):
        count += 1
print(count)
    