import itertools, functools
class puzzle:
    def __init__(self, p):
        self.puzzle_list = p
        self.guess_list = []
        
    def is_solved(self):
        return(all([all(self.puzzle_list[i]) for i in range(9)]))
    
    #both row and column range from 0 to 8
    def row(self,n):
        return(list(self.puzzle_list[n]))
    
    def column(self,n):
        return([self.puzzle_list[i][n] for i in range(9)])
    
    #get box is arranged as follows:
    #012
    #345
    #678
    def box(self, n):
        #black magic functions
        return([self.puzzle_list[3*(n // 3) + i][3*(n % 3) + j] for i,j in itertools.product(range(3), repeat=2)])
    
    def __get_box(self,i,j):
        return(3 * (i // 3) + j // 3)
    
    def pair_exclusions(self,i,j,f):
        paired_exclusions = []
        for s1,s2 in itertools.combinations(f(i,j),2):
            #print(s1,s2)
            if(s1 == s2 and len(s1) == 2):
                paired_exclusions.append(s1)
        if(len(paired_exclusions) == 0):
            return(set())
        return(functools.reduce(lambda x,y:x.union(y),paired_exclusions))
    #Returns the possible set of values for (i,j)
    def __valid_set(self,i,j):
        if(self.puzzle_list[i][j] == 0):
            row_exclusions = set(self.row(i))
            column_exclusions = set(self.column(j))
            box_exclusions = set(self.box(self.__get_box(i,j)))
            v_set = set(range(1,10)) - row_exclusions - column_exclusions - box_exclusions
            return(v_set)
        return(set())
    def valid_set(self,i,j):
        return(self.__valid_set(i,j) - self.pair_exclusions(i,j,self.box_sets)) - self.pair_exclusions(i,j,self.row_sets) - self.pair_exclusions(i,j,self.column_sets)
    def is_solvable(self):
        return(not any([self.valid_set(i,j) == {} and self.puzzle_list[i][j] == 0 for i,j in itertools.product(range(9), repeat = 2)]))
            
        
        
    #returns a list that contains the possible numbers for a given row
    def row_sets(self,n,y):
        return([self.__valid_set(n,i) for i in range(9) if(y != i)])
    
    #returns a list that contains the possible numbers for a given column
    def column_sets(self,x,n):
        return([self.__valid_set(i,n) for i in range(9) if(x != i)])
    
    def box_sets(self,x,y):
        if y is None:
            n = x
            return([self.__valid_set(3*(n//3)+i,3*(n%3)+j) for i,j in itertools.product(range(3), repeat = 2) if(i,j != x,y)])
        else:
            n = self.__get_box(x,y)
            return([self.__valid_set(3*(n//3)+i,3*(n%3)+j) for i,j in itertools.product(range(3), repeat = 2) if(i,j != x,y)])
    
    def __guess(self,i,j,n):
        self.guess_list.append([i,j,n])
        self.puzzle_list[i][j] = n
    
    def __remove_guess(self):
        self.puzzle_list[self.guess_list[-1][0]][self.guess_list[-1][1]] = 0
        self.guess_list.remove(self.guess_list[-1])
    
    def brute_force_solve(self):
        unsolved_squares = [[i,j,self.valid_set(i,j)] for i,j in itertools.product(range(9),repeat = 2) if self.puzzle_list[i][j] == 0]
        unsolved_squares.sort(key=lambda x:len(x[2]))
        for square in unsolved_squares:
            i = square[0]
            j = square[1]
            v_set = square[2]
            for n in v_set:
                #print('guessing %s at (%s,%s)'%(n,i,j))
                self.__guess(i,j,n)
                self.deductive_solve()
                if(self.is_solvable()):
                    if(self.is_solved()):
                        return()
                    self.brute_force_solve()
                while(self.guess_list[-1] != [i,j,n]):
                    self.__remove_guess()
                self.__remove_guess()
    def deductive_solve(self):
        done = False
        while(not done and self.is_solvable()):
            done = True
            for i,j in itertools.product(range(9), repeat = 2):
                x = self.valid_set(i,j)
                if(len(x) == 1):
                    done = False
                    self.__guess(i, j, list(x)[0])
                else:
                    for possible_val in x:
                        if(not possible_val in functools.reduce(lambda x,y:x.union(y),self.box_sets(i,j))):
                            done = False
                            self.__guess(i, j, possible_val)
                        if(not possible_val in functools.reduce(lambda x,y:x.union(y),self.row_sets(i,j))):
                            done = False
                            self.__guess(i, j, possible_val)
                        if(not possible_val in functools.reduce(lambda x,y:x.union(y),self.column_sets(i,j))):
                            done = False
                            self.__guess(i, j, possible_val)
    
    
    def solve(self):
        done = False
        while(not done and self.is_solvable()):
            done = True
            for i,j in itertools.product(range(9), repeat = 2):
                x = self.valid_set(i,j)
                if(len(x) == 1):
                    done = False
                    self.puzzle_list[i][j] = list(x)[0]
                else:
                    for possible_val in x:
                        if(not possible_val in functools.reduce(lambda x,y:x.union(y),self.box_sets(i,j))):
                            done = False
                            self.puzzle_list[i][j] = possible_val
                        if(not possible_val in functools.reduce(lambda x,y:x.union(y),self.row_sets(i,j))):
                            done = False
                            self.puzzle_list[i][j] = possible_val
                        if(not possible_val in functools.reduce(lambda x,y:x.union(y),self.column_sets(i,j))):
                            done = False
                            self.puzzle_list[i][j] = possible_val 

        if(not self.is_solved()):
            print('not solved')
            print(self.puzzle_list)
            print('attempting to brute force')
            self.brute_force_solve()
            print(sum([self.puzzle_list[i].count(0) for i in range(9)]))
    def key(self):
        return(100*int(self.puzzle_list[0][0]) + 10*int(self.puzzle_list[0][1]) + int(self.puzzle_list[0][2]))
#These lines of code read the data from the puzzles and pass them into puzzles
raw = [i[0:-1] for i in open("sudoku.txt").readlines()]
raw[-1] = '000008006'
def getPuzzle(n):
    return([list(map(int,i)) for i in raw[10*n+1:10*(n+1)]])
puzzleSet = [puzzle(getPuzzle(i)) for i in range(50)]



answer = 0
count = 1

for p in puzzleSet:
    print(count)
    count += 1
    p.solve()
    answer += p.key()
print(answer)

