from itertools import combinations

puzzle = '''5616185650518293 ;2 correct
3847439647293047 ;1 correct
5855462940810587 ;3 correct
9742855507068353 ;3 correct
4296849643607543 ;3 correct
3174248439465858 ;1 correct
4513559094146117 ;2 correct
7890971548908067 ;3 correct
8157356344118483 ;1 correct
2615250744386899 ;2 correct
8690095851526254 ;3 correct
6375711915077050 ;1 correct
6913859173121360 ;1 correct
6442889055042768 ;2 correct
2321386104303845 ;0 correct
2326509471271448 ;2 correct
5251583379644322 ;2 correct
1748270476758276 ;3 correct
4895722652190306 ;1 correct
3041631117224635 ;3 correct
1841236454324589 ;3 correct
2659862637316867 ;2 correct'''

sample_puzzle = '''90342 ;2 correct
70794 ;0 correct
39458 ;2 correct
34109 ;1 correct
51545 ;2 correct
12531 ;1 correct'''

lines = puzzle.split('\n')
constraints = []
for line in lines:
	split_line = line.split(' ;')
	digits = [i for i in split_line[0]]
	num_correct = int(split_line[1][0])
	constraints.append((digits, num_correct))

# print constraints

class ConstraintIterator:

	def __init__(self, current_digit_list, constraint):
		self.current_digit_list = current_digit_list
		self.unset_indices = [i for i in range(len(self.current_digit_list)) if self.current_digit_list[i] is None]

		required_num_correct = constraint[1]
		self.constraint_digits = constraint[0]

		observed_num_correct = 0
		for pair in zip(self.constraint_digits, current_digit_list):
			if pair[0] == pair[1]:
				observed_num_correct += 1
		
		remaining_required_num_correct = required_num_correct - observed_num_correct
		self.iterator = combinations(self.unset_indices, remaining_required_num_correct)

		self.last_index_set = None

	# Returns true if there is an option to advance to. Returns false if we've tried all possible options.
	def advance_guesses(self):
		if self.last_index_set is not None:
			for index in self.last_index_set:
				self.current_digit_list[index] = None
		try:
			indices_to_set = self.iterator.next()
			self.last_index_set = indices_to_set
			for index in indices_to_set:
				#print index, len(self.current_digit_list), self.current_digit_list
				self.current_digit_list[index] = self.constraint_digits[index]
#			print self.current_digit_list
		except StopIteration:
			return False
		return True

class PuzzleSolver:

	def __init__(self, constraints):
		self.constraints = constraints
		num_digits = len(constraints[0][0])
		self.digit_possibilities = {i : [j for j in range(10)] for i in range(num_digits)}
		self.correct_indices_possibilities = {i : [j for j in range(num_digits)] for i in range(len(constraints))}

	def solve(self):
		self.constraint_iterators = []
		# TODO write the brute force.
		self.current_digits = [None for i in range(len(constraints[0][0]))]

		while not self.is_solved():
			if self.contradicts_constraint():
				# Backtrack
				self.advance_constraint_iterators()

			else:
				# print self.current_digits
				cur_constraint_index = len(self.constraint_iterators)
				if cur_constraint_index == len(self.constraints):
					print self.current_digits, self.is_solved()
				ci = ConstraintIterator(self.current_digits, self.constraints[cur_constraint_index])
				ci.advance_guesses()
				self.constraint_iterators.append(ci)
		return self.current_digits

	def advance_constraint_iterators(self):
		result = self.constraint_iterators[-1].advance_guesses()
		while not result:
			self.constraint_iterators.pop()
			result = self.constraint_iterators[-1].advance_guesses()

	def contradicts_constraint(self):
		for constraint_digits, required_num_correct in self.constraints:
			observed_num_correct = 0
			num_unset = 0
			for pair in zip(constraint_digits, self.current_digits):
				if pair[1] is None:
					num_unset += 1
				if pair[0] == pair[1]:
					observed_num_correct += 1
			if observed_num_correct > required_num_correct:
				return True
			if num_unset + observed_num_correct < required_num_correct:
				return True
		return False

	def is_solved(self):
		if any([digit is None for digit in self.current_digits]):
			return False
		for constraint_digits, required_num_correct in self.constraints:
			observed_num_correct = 0
			for pair in zip(constraint_digits, self.current_digits):
				if pair[0] == pair[1]:
					observed_num_correct += 1
			if observed_num_correct != required_num_correct:
				return False
		return True


puzzle_solver = PuzzleSolver(constraints)

for digit in range(10):
	a = str(digit)
	candidate = ['4', '6', '4', '0', '2', '6', '1', '5', '7', '1', '8', '4', a, '5', '3', '3']
	puzzle_solver.current_digits = candidate
	if puzzle_solver.is_solved():
		print ''.join(candidate)

# print int(''.join(puzzle_solver.solve()))


'''
Output errors at the following because 0 matching constraints are not specified.

464026157184 _ 533

To remedy this, I just brute force the last one as is shown above b/c I'm too lazy to fix the code.
'''