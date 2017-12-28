'''
A number n with prime factorization \prod p_i^{\alpha_i} has sigma(n) equal to

\prod (p_i^{\alpha_i + 1} - 1) / (p_i - 1).

Also note 2017 is prime.

So we can look over all primes and potential values of \alpha_i where (p_i^{\alpha_i + 1} - 1) / (p_i - 1) is divisible by 2017.

Since the product over such primes has to be pretty small (10^11), we know that most primes can't have \alpha_i bigger than 3 or so.

wait holy shit this gets annoying once you have the base numbers--you have to multiply by shit and do inclusion exclusion or something. that's awful. nvm.

'''


from helpers import isPrimeMR



limit = 10**6



