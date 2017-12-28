from helpers import sieve
'''
Scratch work:
x = k + k/p + n/p^2 + ... = k(1 + 1/p + 1/p^2 + 1/p^3 + ...) = k/(1 - 1/p)
= kp/(p-1)
= n/(p-1)
n = (p-1)x
n = pk


After 20 hours of computation, gives answer
278157919195482643
'''
N = 10**6
c = 1234567890

memo = {}
def num_fac_powers(p, i):
    if (p, i) in memo:
        return memo[(p, i)]
    if i < p:
        return 0
    a = num_fac_powers(p, i / p)
    if len(memo) > 100000:
        memo.clear()
    memo[(p, i)] = i/p + a
    return i/p + a

def get_smallest_possible(p, i):
    min_possible_power = c * num_fac_powers(p, i)
    potential_n = p + p * (((p - 1) * min_possible_power) / p)
    while num_fac_powers(p, potential_n) < min_possible_power:
        potential_n += p
    return potential_n

primes = sieve(N)
setprimes = set(primes)

print len(primes)
last_chosen_p = 1


last_chosen_p = 1
answer = 0
for i in range(N, 9, -1):
    if i % 100 == 0:
        print i
    if (i+1)/last_chosen_p == i/last_chosen_p and i < N:
        answer += get_smallest_possible(last_chosen_p, i)
        continue
    
    n = 0
    for p in primes:
        if p > i:
            break
        potential_n = get_smallest_possible(p, i)
        if potential_n > n:
            chosen_p = p
            n = potential_n
    #print 'for i = %s prime was %s'%(i, chosen_p)
    last_chosen_p = chosen_p
    
    answer += n
    answer %= 10**18

print answer
