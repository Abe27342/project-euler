from helpers import sieve, isPrimeMR
from itertools import product, combinations

number_len = 10
answer = 0
for digit in range(10):
    num_replacements = 1
    
    other_digits = [str(i) for i in range(10)]
    other_digits.remove(str(digit))
    primes_not_found = True
    while primes_not_found:
        # Generate order digits to go in the number
        for perm in product(other_digits, repeat = num_replacements):
            # Then generate combinations for which places those digits go
            for comb in combinations(range(number_len), num_replacements):
                l = [str(digit)] * number_len
                for i in range(num_replacements):
                    l[comb[i]] = perm[i]
                possible_prime = int(''.join(l))
                if possible_prime > 10**(number_len - 1):
                    if isPrimeMR(possible_prime):
                        primes_not_found = False
                        print possible_prime
                        answer += possible_prime
        num_replacements += 1


print answer
