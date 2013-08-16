from helpers import fibs
l = []

count = 0
for x in range(1,2**30+1):
    if(x ^ (2*x) ^ (3*x) == 0):
        count += 1
l.append(count)
print(l)
print(fibs(32))