from helpers import isPalindrome

def reverse(s):
    return(int(str(s)[::-1]))

def isLychrel(n):
    count = 0
    while(count < 100):
        n = n + reverse(n)
        if(isPalindrome(n)):
            return(False)
        count += 1
    return(True)

print len([x for x in range(1, 10000) if isLychrel(x)])