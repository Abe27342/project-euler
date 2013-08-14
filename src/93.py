import itertools
operations = ['+','-','*','/']

def result(input_set, op_set):
    mi = [str(i) for i in input_set]
    mo = [str(i) for i in op_set]
    r1 = eval('((' + mi[0] + mo[0] + mi[1] + ')' + mo[1] + mi[2] + ')' + mo[2] + mi[3])
    r2 = eval('(' + mi[0] + mo[0] + mi[1] + ')' + mo[1] + '(' + mi[2] + mo[2] + mi[3] + ')')
    if(int(r1) != r1 or r1 < 1):
        r1 = 0
    if(int(r2) != r2 or r2 < 1):
        r2 = 0
    r1 = set([int(r1)])
    r2 = set([int(r2)])
    return(r1.union(r2) - {0})

def get_longest_chain(s):
    length = 1
    while(all([i in s for i in range(1,length)])):
        length += 1
    length -= 2
    return(length)

op_sets = [i for i in itertools.product(operations, repeat=3)]
max_length = []
doesnt_contain_24 = []
for digit_set in itertools.combinations(range(1,10), 4):
    possible_vals = set()
    for input_set in itertools.permutations(digit_set):
        for op_set in op_sets:
            possible_vals = possible_vals.union(result(input_set,op_set))
    if(24 not in possible_vals):
        doesnt_contain_24.append(digit_set)
    max_length.append([digit_set,get_longest_chain(possible_vals)])

max_length.sort(key = lambda x:x[1], reverse = True)
print(max_length)
print(doesnt_contain_24)