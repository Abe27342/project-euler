
w = eval('[' + open('98words.txt').readlines()[0] + ']')

#print(w)

def get_digit_list(n):
    l = []
    for i in str(n):
        if(l.count([i,str(n).count(i)]) == 0):
            l.append([i,str(n).count(i)])
    l.sort()
    return(l)

def get_character_set(s):
    l = []
    for i in s:
        if(l.count([i,s.count(i)]) == 0):
            l.append([i,s.count(i)])
    l.sort()
    return(l)

w.sort(key=lambda x:get_character_set(x))


def get_possible_squares(n):
    squares = [i**2 for i in range(int((10**n)**0.5)+2) if 10**(n-1)-1 < i**2 < 10**n]
    squares.sort(key=lambda x:get_digit_list(x))
    i = 0
    split_squares = []
    while(i < len(squares)):
        c = 0
        original_d_list = get_digit_list(squares[i])
        m = []
        while(i + c < len(squares) and original_d_list == get_digit_list(squares[i+c])):
            m.append(squares[i+c])
            c += 1
        if(len(m) > 1):
            split_squares.append(m)
        i += c
    return(split_squares)
    
def match_square_to_word(word,square):
    square = str(square)
    d = {}
    for i in range(len(word)):
        if(d.get(word[i]) == None):
            d[word[i]] = square[i]
        else:
            if(d.get(word[i]) != square[i]):
                return(None)
    #check for every different char maps to a different digit
    l = [x[1] for x in d.items()]
    for i in range(len(l)):
        if(l.count(l[i]) > 1):
            return(None)
    return(d)
    


i = 0
split_w = []
while(i < len(w)):
    c = 0
    original_char_set = get_character_set(w[i])
    m = []
    while(i+c < len(w) and original_char_set == get_character_set(w[i+c])):
        m.append(w[i+c])
        c += 1
    if(len(m) > 1):
        split_w.append(m)
    i+= c



for word_pair in split_w:
    if(len(word_pair[0]) == 2):
        continue
    for square_list in get_possible_squares(len(word_pair[0])):
        for square in square_list:
            d = match_square_to_word(word_pair[0],square)
            if(d != None):
                word2 = int(''.join([d.get(i) for i in word_pair[1]]))
                if(word2**0.5 == int(word2**0.5)):
                    print(word_pair,square, word2)

print(get_possible_squares(4))