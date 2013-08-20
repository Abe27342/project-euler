import itertools
matrix_height = 80
matrix_width = 80

start = ['start',0]
finish = ['finish',1000000000]

def neighbors(square):
    if(square == finish):
        yield()
    elif(square == start):
        for i in range(matrix_height):
            yield [i,0]
    elif(square[1] == matrix_width-1):
        yield(finish)
    
    else:
        if(square[0] > 0):
            yield [square[0]-1,square[1]]
        if(square[0] < matrix_height - 1):
            yield [square[0]+1,square[1]]
        if(square[1] < matrix_width - 1):
            yield [square[0],square[1]+1]


def get_minimum_square(list_of_squares, distance_from_start):
    minimum = 1000000000
    min_square = [0,0]
    for square in list_of_squares:
        if(square == finish):
            if(finish[1] < minimum):
                minimum = finish[1]
                min_square = finish
        elif(distance_from_start[square[0]][square[1]] < minimum):
            minimum = distance_from_start[square[0]][square[1]]
            min_square = square
    return(min_square)

#implements dijkstra's algorithm on a rectangular matrix
def find_minimal_path_sum(start_square,target_square,matrix):
    distance_from_start = []
    for i in range(matrix_height):
        distance_from_start.append([])
        for j in range(matrix_width):
            distance_from_start[i].append(1000000000)
    #print(distance_from_start)
    #distance_from_start[start_square[0]][start_square[1]] = 0        
    #print(distance_from_start[79][79])
    unchecked_squares = [[i[0],i[1]] for i in itertools.product(range(matrix_height),range(matrix_width))]
    unchecked_squares.extend([finish,start])
    checked_squares = []
    
    current_square = start_square
    
    while(target_square in unchecked_squares):
        for neighboring_square in neighbors(current_square):
            #print(current_square,neighboring_square)
            if(current_square == finish):
                break
            elif(neighboring_square == finish):
                if(distance_from_start[current_square[0]][current_square[1]] + matrix[current_square[0]][current_square[1]] < finish[1]):
                    finish[1] = distance_from_start[current_square[0]][current_square[1]] + matrix[current_square[0]][current_square[1]]
            elif(current_square == start):
                distance_from_start[neighboring_square[0]][neighboring_square[1]] = 0
            elif(distance_from_start[current_square[0]][current_square[1]] + matrix[current_square[0]][current_square[1]] < distance_from_start[neighboring_square[0]][neighboring_square[1]]):
                #print(current_square)
                distance_from_start[neighboring_square[0]][neighboring_square[1]] = distance_from_start[current_square[0]][current_square[1]] + matrix[current_square[0]][current_square[1]]
        
        checked_squares.append(current_square)
        unchecked_squares.remove(current_square)
        current_square = get_minimum_square(unchecked_squares,distance_from_start)
    #answer = matrix[target_square[0]][target_square[1]] + distance_from_start[target_square[0]][target_square[1]]
    return(finish[1])
    
x = open('matrix.txt').readlines()
y = [eval('[' + x[i] + ']') for i in range(len(x))]

print(find_minimal_path_sum(start,finish,y))