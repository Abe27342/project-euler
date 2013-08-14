from collections import Counter

x = eval('[' + open('cipher1.txt').readlines()[0] + ']')
#print sum([sum([[Counter([x[0::3],x[1::3],x[2::3]][j]).most_common(1)[0][0] for j in range(3)][n] ^ 32 ^ [x[0::3],x[1::3],x[2::3]][n][m] for m in range(len())]) for n in range(3)])
#print sum([])
print sum([sum([ord(' ') ^ [Counter(x[j::3]).most_common(1)[0][0] for j in range(3)][i] ^ x[i::3][m] for m in range(len(x[i::3]))]) for i in range(3)])
print x[0::3], x[1::3]

'''
here are the ideas that motivated the one liner...even if it is a piece of shit
print len(x)

first = [x[3*k] for k in range(401)]
second = [x[3*k+1] for k in range(400)]
third = [x[3*k+2] for k in range(400)]

first_e = Counter(first).most_common(1)
second_e = Counter(second).most_common(1)
third_e = Counter(third).most_common(1)


f_un = [chr(first[i] ^ 32 ^ first_e[0][0]) for i in range(401)]
s_un = [chr(second[i] ^ 32 ^ second_e[0][0]) for i in range(400)]
t_un = [chr(third[i] ^ 32 ^ third_e[0][0]) for i in range(400)]
print first_e[0][0]
print second_e
print third_e
y = [[f_un[k],s_un[k],t_un[k]] for k in range(400)]
print(y)
'''