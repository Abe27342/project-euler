import random
square_frequency = [[0,i] for i in range(40)]
#returns [roll,isDoubles()]
def get_random_permutation(s):
    unused_list = s
    perm = []
    while(len(unused_list) > 0):
        next_index = random.randint(0,len(unused_list)-1)
        perm.append(unused_list[next_index])
        unused_list.remove(unused_list[next_index])
    return(perm)

def draw_card(deck):
    card = deck[0]
    deck.remove(card)
    deck.append(card)
    return(card)

chance_deck = get_random_permutation([i for i in range(1,17)])
community_deck = get_random_permutation([i for i in range(1,17)])

def get_dice_roll():
    a = random.randint(1,4)
    b = random.randint(1,4)
    return([a+b,a==b])

def take_turn(initial_square, num_of_doubles):
    dice_roll = get_dice_roll()
    
    #if you roll three doubles, go to jail yo
    if(num_of_doubles == 2 and dice_roll[1] == True):
        return(10)
    
    #add dat roll
    new_square = (initial_square + dice_roll[0]) % 40
    #rules for various squares
    
    #if we land on go to jail, go to jail bitch
    if(new_square == 30):
        return(10)
    
    #if we land on community chest, draw from the community chest deck and face the consequences
    if(new_square in {2,17,33}):
        card_number = draw_card(community_deck)
        if(card_number == 1):
            new_square = 0
        elif(card_number == 2):
            return(10)
    
    #if we land on chance, draw from the chance deck and face the consequences
    if(new_square in {7,22,36}):
        card_number = draw_card(chance_deck)
        if(card_number == 1):
            new_square = 0
        elif(card_number == 2):
            return(10)
        elif(card_number == 3):
            new_square = 11
        elif(card_number == 4):
            new_square = 24
        elif(card_number == 5):
            new_square = 39
        elif(card_number == 6):
            new_square = 5
        elif(card_number in {7,8}):
            new_square += (5-new_square) % 10
            new_square = new_square % 40
        elif(card_number == 9):
            if(new_square == 7):
                new_square = 12
            else:
                new_square = 28
        elif(card_number == 10):
            new_square -= 3
            #if we want to be pedantic we should draw community chest cards here in some cases but i'm too lazy
    #if we rolled doubles, go again!
    if(dice_roll[1] == True):
        return(take_turn(initial_square+dice_roll[0],num_of_doubles+1))
    
    return(new_square)



#monopoly! yay

def run_simulation(turns):
    current_square = 0
    for i in range(turns):
        current_square = take_turn(current_square,0)
        square_frequency[current_square][0] += 1

run_simulation(1000000)
square_frequency.sort(key=lambda x:x[0],reverse = True)
print(square_frequency)
    

