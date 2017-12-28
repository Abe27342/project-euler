from decimal import *
getcontext().prec = 20

'''
Define f(a, b, k, n) to be the probability of randomly distributing
the k remaining defects amongst the n chips such that no chip has more than
two defects, if there are already 'a' chips with one defect and 'b' chips
with two defects. f(0, 0, 20000, 10**6) is what we want. Evidently f satisfies
the recursion

f(a, b, k, n) = (n - a - b)/n * f(a+1, b, k-1, n) + a/n * f(a, b+1, k-1, n)
'''
n = 10**6
k = 2*10**4

memo = {}
def f(a,b,k,n):
    if (a,b,k,n) in memo:
        return memo[(a,b,k,n)]
    if k == 0:
        return 1
    part1 = Decimal(n - a - b)/n * f(a + 1, b, k - 1, n)
    part2 = Decimal(a)/n * f(a - 1, b + 1, k - 1, n)
    memo[(a,b,k,n)] = part1 + part2
    return part1 + part2
# f[i][j] contains the probability that k - i - 2j defects go onto the
# n chips s.t. there are no more than 2 defects per chip if there are already
# i chips with 1 defect and j chips with 2 defects.
# f[i][j] = 1/n * ((n - i - j) f[i+1, j] + i f[i - 1, j + 1])
'''
f = [[float(1) for j in range(1 + (k - i)/2)] for i in range(k + 1)]
print f
for j in range(k/2, -1, -1):
    if j % 100 == 0:
        print j
    for i in range(k - 2 * j - 1, -1, -1):
        if i == 0:
            f[i][j] = float(1)/n * ((n - i - j) * f[i + 1][j])
            continue
        f[i][j] = float(1)/n * ((n - i - j) * f[i + 1][j] + i * f[i - 1][j + 1])
'''
currColumn = [0, 0, 1]
nextColumn = [1]

for j in range(k/2 - 1, -1, -1):
    if j % 100 == 0:
        print j
    for i in range(len(currColumn) - 2, -1, -1):
        if i == 0:
            currColumn[i] = float(1)/n * ((n - i - j) * currColumn[i+1])
            continue
        currColumn[i] = float(1)/n * ((n - i - j) * currColumn[i+1] + i * nextColumn[i-1])
    currColumn,nextColumn = nextColumn,currColumn
    currColumn.extend([0, 0, 0, 1])

print 1 - nextColumn[0]


currColumn = [0, 0, 1]
nextColumn = [1]

for j in range(k/2 - 1, -1, -1):
    if j % 100 == 0:
        print j
    for i in range(len(currColumn) - 2, -1, -1):
        if i == 0:
            currColumn[i] = 1/Decimal(n) * ((n - i - j) * currColumn[i+1])
            continue
        currColumn[i] = 1/Decimal(n) * ((n - i - j) * currColumn[i+1] + i * nextColumn[i-1])
    currColumn,nextColumn = nextColumn,currColumn
    currColumn.extend([Decimal(0), Decimal(0), Decimal(0), Decimal(1)])

print 1 - nextColumn[0]


# had to recode the shit out of this problem to avoid awful memory usage. Still slow as hell since
# python decimals are slow. In theory shouldn't be so dang bad--needs roughly 8e8 operations.
# Output: 0.73117202512829605994
#         0.7311720251
