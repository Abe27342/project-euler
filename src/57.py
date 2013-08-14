a,b = 3,2
answer = 0
count = 1
while count < 1001:
    a,b = 2*b+a,a+b
    if len(str(a)) > len(str(b)):
        answer += 1
    count += 1
print(answer)

