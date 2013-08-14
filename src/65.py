import fractions
def get_frac(continued_fraction_list):
    x = continued_fraction_list[::-1]
    y = fractions.Fraction(x[0])
    x.remove(x[0])
    while(len(x) > 0):
        y = x[0] + 1/y
        x.remove(x[0])
    return(y)
def get_continued_frac(n, de):
    d = fractions.Fraction(n,de)
    x = []
    while(int(d) != d):
        x.append(int(d))
        d = 1/(d-int(d))
    x.append(int(d))
    return(x)
def sum_of_digits(n):
    return(sum([int(i) for i in str(n)]))


e = [1]*100
e[0] = 2
for i in range(1,34):
    e[3*i-1] = 2*i
print sum_of_digits(get_frac(e).numerator)