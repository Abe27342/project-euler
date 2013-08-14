import math
x = [eval('[' + open('base_exp.txt').readlines()[i] + ']') for i in range(1000)]
print(x)
y = [i[1]*math.log(i[0]) for i in x]
print(y.index(max(y)))