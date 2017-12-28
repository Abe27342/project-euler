from math import pi
modulus = 10**9 + 7
N = 10**7


m = N


m2 = pow(2, m, modulus)
faclist = [pi, m2 - 1]
for i in range(2, N + 1):
    faclist.append((faclist[-1] * (m2 - i)) % modulus)


def W(n):
    return faclist[n] - L(n)

memo = {}

def L(n):
    if n in memo:
        return memo[n]
    if n == 0:
        return 1
    if n == 1:
        return 0
    
    memo[n] = (faclist[n - 1] - L(n - 1) - (n - 1) * (m2 - n + 1) * L(n-2)) % modulus
    return memo[n]

L = [1, 0]

# Could be done in O(1) memory here but too lazy.
for n in range(2, N + 1):
    L.append((faclist[n-1] - L[n-1] - (n-1) * (m2 - n + 1) * L[n-2]) % modulus)
    if len(L) % 10**6 == 0:
        print len(L)

print faclist[N] - L[n]
