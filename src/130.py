from helpers import gcd

def o(n):
    answer = 1
    while(pow(10,answer,9*n) != 1):
        answer += 1
    return(answer)
done = False
count = 1000000
while(not done):
    if(gcd(10,count) == 1 and o(count) > 1000000):
        print('answer = ',count)
        done = True
        break
    count += 1