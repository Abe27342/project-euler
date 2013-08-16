def get(m, x, y):
    if(x < 0 or y < 0 or x >= len(m) or y >= len(m[0])):
        return(10**9)
    else:
        return(m[x][y])
def solve(m):
    #assumes that the matrix is a rectangle
    for i in range(len(m)):
        for j in range(len(m[0])):
            if(not (i == 0 and j == 0)):
                m[i][j] += min([get(m,i,j-1), get(m,i-1,j)])
    print(m)
    return(m[-1][-1])

def solve82(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
            if(not (i == 0 and j == 0)):
                m[i][j] += min([get(m,i,j-1), get(m,i-1,j)])
    print(m)
    return(m[-1][-1])

x = open('matrix.txt').readlines()
#print(x[0])
y = [eval('[' + x[i] + ']') for i in range(len(x))]
print(solve(y))