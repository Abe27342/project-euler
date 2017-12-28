# Anything that seems like it could be reused in more than one problem goes here.

# Sieve of Eratosthenes, finds all primes less than n
def sieve(n):
    if n == 10**8:
        fp = open('primes_10^8.txt')
        ans = [int(line[:-1]) for line in fp.readlines()]
        fp.close()
        return ans
    s = [False]*2 + [True]*(n-2)
    lim = len(s) ** 0.5
    for p,b in enumerate(s):
        if p > lim:
            break
        if not b:
            continue
        for i in range(2*p,len(s),p):
            s[i] = False
    return [i for (i, b) in enumerate(s) if b]

def euler_totient(pf):
    answer = 1
    for (prime, power) in pf.items():
        answer *= (prime - 1) * prime**(power - 1)
    return answer

def sieve_euler_phi(n):
    primes = sieve(n)
    totients = [1] * (n + 1)
    for p in primes:
        for i in range(p, n, p):
            k = i / p 
            e = 1
            f = p - 1
            while k % p == 0:
                k /= p
                f *= p 
                e += 1
            totients[i] *= f
    return totients

def memoize(f):
    memo = {}
    def helper(*args):
        if args not in memo:            
            memo[args] = f(*args)
        return memo[args]
    return helper

# returns the sum of the totient function from 1 to n using black magic mobius inversion.
@memoize
def sum_totient(n):
    if n == 1:
        return 2
    else:
        total = (n + 3) * n / 2
        d = 2
        while d < n + 1:
            multiplier = 1
            increment = 1
            while n / d == n / (d + multiplier):
                multiplier *= 2
            if multiplier % 2 == 0:
                multiplier /= 2

            total -= multiplier * sum_totient(n / d)
            d += multiplier
        return total



# Miller-Rabin style primality test, based on pseudo-code from
# https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
# Correct for n < 18,446,744,073,709,551,616.
def isPrimeMR(n):
    assert n < 18446744073709551616L
    if n < 2 or (n > 2 and n % 2 == 0):
        return False
    if n in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]:
        return True
    r = 0
    d = n - 1
    while d % 2 == 0:
        d /= 2
        r += 1
    for a in [2, 3, 5, 7, 11, 13, 17]:
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        temp_r = r
        while temp_r > 1:
            x = pow(x, 2, n)
            if x == 1:
                return False
            if x == n-1:
                break
            temp_r -= 1
        if temp_r == 1:
            return False
    return True
        

def isPrime(n):
    return all([n > 1] + [n % 2 != 0] + [n % 3 != 0] + [n % (6*i+1) != 0 and n % (6*i-1) != 0 for i in range(1,int((n**0.5+6)/6))])

pl = sieve(100000)
def isPrimeSieve(n):
    global pl
    if n >= len(pl)**2:
        pl = sieve(int(n**0.5+1))
    return all([n % p != 0 for p in pl])

fl = [1,1,2,3,5]

# Returns the first n Fibonacci numbers
def fibs(n):
    while n > len(fl):
        fl.append(fl[-1] + fl[-2])
    return fl[:n]

def fib(n):
    while n > len(fl):
        fl.append(fl[-1] + fl[-2])
    return fl[n-1]

# '123' -> ['123','231','312']
def rotations(s):
    for i in range(len(s)):
        yield s
        s = s[1:]+s[0]
        
def isPalindrome(n):
    n = str(n)
    if n == n[::-1]:
        return True
    else:
        return False

def gcd(a,b):
    if(a == 0):
        return(b)
    if(b == 0):
        return(a)
    if(a == b):
        return(a)
    if(a > b):
        return(gcd(b,a % b))
    if(b > a):
        return(gcd(a,b % a))

class PrimeFactorization:
    def __init__(self, n):
        self.n = n
        self.prime_powers = {}
        return

    def split_on_prime(self, prime):
        assert self.n % prime == 0
        power = 0
        while self.n % prime == 0:
            power += 1
            self.n /= prime
        self.prime_powers[prime] = power

    def is_fulfilled(self):
        return self.n == 1

    def __repr__(self):
        return self.prime_powers.__repr__()


# returns a list of the prime factorizations up to n
def prime_factorizations(N):
    prime_factorizations = [PrimeFactorization(n) for n in range(N)]
    s = [False]*2 + [True]*(N - 2)
    for p,b in enumerate(s):
        if not b:
            continue
        prime_factorizations[p].split_on_prime(p)
        for i in range(2*p,len(s),p):
            s[i] = False
            prime_factorizations[i].split_on_prime(p)
    return [p.prime_powers for p in prime_factorizations]



# see note on recurrence_matrix to see input style of coeffs. for fibonacci, coeffs are [1,1] and x0 = [[1], [1]].
def solve_recurrence(coeffs, x0, n, modulus):
    xn = mult(fast_power_iterative(recurrence_matrix(coeffs), n, modulus), x0, modulus)
    return xn[-1][0]

# multiplies the matrices A and B, represented as double lists and taken modulo the modulus
# if modulus is -1, ignores.
def mult(A, B, modulus):
    common_dim = len(A[0])
    m = len(A)
    n = len(B[0])
    assert len(A[0]) == len(B)

    #product is an m by n matrix
    product = [[0 for i in range(n)] for j in range(m)]
    for i in range(m):
        for j in range(n):
            for k in range(common_dim):
                product[i][j] += A[i][k] * B[k][j]
                if modulus != -1:
                    product[i][j] %= modulus
    return product

def dirac(pred1, pred2):
    # assert pred1 in [True, False]
    # assert pred2 in [True, False]
    if pred1 == pred2:
        return 1
    else:
        return 0

def fast_power(A, n, modulus):
    if n == 0:
        return [[dirac(i, j) for i in range(len(A))] for j in range(len(A))]
    if n == 1:
        return A
    halfA = fast_power(A, n // 2, modulus)
    
    if n % 2 == 0:
        return mult(halfA, halfA, modulus)
    else:
        return mult(mult(halfA, halfA, modulus), A, modulus)


def fast_power_iterative(A, n, modulus):
    result = [[dirac(i, j) for i in range(len(A))] for j in range(len(A))]
    
    while n > 0:
        if n % 2 == 1:
            result = mult(result, A, modulus)
        A = mult(A, A, modulus)
        n /= 2
    return result

# For a recurrence of the form a_n = \sum c_{n-i} a_{n-i}, the coeffs list should be [c_{n-1}, c_{n-2}, \cdots].
def recurrence_matrix(coeffs):
    A = [coeffs]
    A.extend([[0 for i in range(len(coeffs))] for j in range(len(coeffs) - 1)])
    for i in range(len(coeffs) - 1):
        A[i + 1][i] = 1
    return A


# these taken from here: http://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

# this taken from here: https://github.com/sigh/Python-Math/blob/master/ntheory.py
def crt(items):
  """Solve the chinese remainder theorem
  Given a list of items (a_i, n_i) solve for x such that x = a_i (mod n_i)
  such that 0 <= x < product(n_i)
  Assumes that n_i are pairwise co-prime.
  """

  # Determine N, the product of all n_i
  N = 1
  for a, n in items:
    N *= n

  # Find the solution (mod N)
  result = 0
  for a, n in items:
    m = N//n
    d, r, s = egcd(n, m)
    if d != 1:
        print s, r, d, items
        raise "Input not pairwise co-prime"
    result += a*s*m

  # Make sure we return the canonical solution.
  return result % N



'''

Not meant for import. setprimes needs to be all primes up to the limit of the prime factors you want to get.
def get_pf(n):
    if n < len(pfs):
        return pfs[n]
    else:
        if n in setprimes:
            return {n : 1}
        ans = {}
        for p in primes:

            if n < len(pfs) or n in setprimes:
                break
            power = 0
            while n % p == 0:
                power += 1
                n /= p 

            if power > 0:
                ans[p] = power 

        if n in setprimes:
            ans[n] = 1
        elif n > 1:
            recursive_ans = {k : v for (k, v) in pfs[n].items()}
            for (prime, power) in ans.items():
                if prime in recursive_ans:
                    recursive_ans[prime] += power
                else:
                    recursive_ans[prime] = power

            return recursive_ans 

        return ans

'''