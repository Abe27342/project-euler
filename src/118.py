from helpers import isPrimeMR
from itertools import permutations

primes = []

# No pandigital 9 digit primes b/c they're all divisible by 3.
for num_digits in range(1, 9):
    print num_digits
    for p in permutations('123456789', num_digits):
        if isPrimeMR(int(''.join(p))):
            primes.append(int(''.join(p)))

print len(primes)

class PrimeCounter:
    def __init__(self):
        self._index = 0
        self.mpdigits_numprimes = {}

    def increase_digitcount(self, digitset):
        if digitset in self.mpdigits_numprimes:
            (index, count) = self.mpdigits_numprimes[digitset]
            self.mpdigits_numprimes[digitset] = (index, count + 1)
        else:
            self.mpdigits_numprimes[digitset] = (self._index, 1)
            self._index += 1

def digitset(n):
    return frozenset([i for i in str(n)])

pc = PrimeCounter()

for p in primes:
    pc.increase_digitcount(digitset(p))

mpdigits_numprimes = pc.mpdigits_numprimes

print len(mpdigits_numprimes)
# print mpdigits_numprimes


def count(cur_dict, cur_digit_set, cur_min_index):
    if frozenset([str(i) for i in range(1, 10)]) == cur_digit_set:
        return 1
    newdict = {key : value for (key, value) in cur_dict.items() if len(key.intersection(cur_digit_set)) == 0 and value[0] > cur_min_index}
    total = 0
    for (new_digits, (min_index, prime_count)) in newdict.items():
        total += prime_count * count(newdict, cur_digit_set.union(new_digits), min_index)
    return total

print count(mpdigits_numprimes, frozenset(), -1)
