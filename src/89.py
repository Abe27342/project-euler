def simplify(s):
    if('I'*5 in s):
        s = s.replace('I'*5,'V')
    if('VV' in s):
        s = s.replace('VV','X')
    if('X'*5 in s):
        s = s.replace('X'*5,'L')
    if('LL' in s):
        s = s.replace('LL','C')
    if('C'*5 in s):
        s = s.replace('C'*5,'D')
    if('DD' in s):
        s = s.replace('DD','M')
    #I pair rules
    if('VIIII' in s):
        s = s.replace('VIIII','IX')
    if('IIII' in s):
        s = s.replace('IIII','IV')
    #X pair rules
    if('LXXXX' in s):
        s = s.replace('LXXXX','XC')
    if('XXXX' in s):
        s = s.replace('XXXX','XL')
    #C pair rules
    if('DCCCC' in s):
        s = s.replace('DCCCC','CM')
    if('CCCC' in s):
        s = s.replace('CCCC','CD')
    
    return(s)
x = [str(open('roman.txt').readlines()[i])[0:-1] for i in range(1000)]
x[-1] = 'XXXXVIIII'

count = 0
for s in x:
    count += len(s) - len(simplify(s))
print(count)
#print(x)
#print(simplify('XXXXIX'))
        