import fractions
from helpers import gcd
def get_frac(continued_fraction_list):
    x = continued_fraction_list[::-1]
    y = fractions.Fraction(x[0])
    x.remove(x[0])
    while(len(x) > 0):
        y = x[0] + 1/y
        x.remove(x[0])
    return(y)
#returns the periodic fraction of sqrt(n)
def get_periodic_fraction(n):
    l = []
    num_part_1 = 1
    num_part_2 = -int(n**0.5)
    den = 1
    l.append([int(n**0.5),den,num_part_1,num_part_2])
    while(l.count(l[-1]) == 1):
        den,num_part_1,num_part_2 = num_part_1**2*n-num_part_2**2,num_part_1*den,-den*num_part_2
        l.append([int((num_part_1*n**0.5+num_part_2)/den),den,num_part_1,num_part_2])
        #print(l)
        num_part_2 -= den*l[-1][0]
        d = gcd(gcd(abs(den),abs(num_part_1)),gcd(abs(den),abs(num_part_2)))
        den,num_part_1,num_part_2 = int(den/d),int(num_part_1/d),int(num_part_2/d)
        #print(den,num_part_1,num_part_2)
    x = [l[i][0] for i in range(len(l)-1)]
    return(x)

#print(get_periodic_fraction(5))

#print(get_frac(get_periodic_fraction(5)))

def get_first_soln(n):
    done = False
    count = 2
    x = get_periodic_fraction(n)
    while(not done):
        if(count > len(x)):
            for i in range(1,len(x)):
                x.append(x[i])
        y = get_frac(x[0:count])
        if(y.numerator**2 - n*y.denominator**2 == 1):
            done = True        
        count += 1
    return([y.numerator,y.denominator])

#print(get_first_soln(1923))
answer_set = [[get_first_soln(d),d] for d in range(2,1000) if d**0.5 != int(d**0.5)]
answer_set.sort(key=lambda x:x[0][0],reverse=True)
print(answer_set[0][1])

    