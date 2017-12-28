

n_max = 10**5


# Tests if r is a root of P_n(x), where P_n(x) given in problem statement.
def test_root(n, r):
    n_listed = [int(i) for i in str(n)]
    return reduce(lambda x,y : r * x + y, n_listed) == 0

for n in range(1, n_max):
    if test_root(n, -5):
        print n
