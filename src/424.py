from itertools import product, chain, combinations
from string import maketrans


def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

class SumPossibilities:

	def __init__(self):
		self.possibleNumbers = {i : {} for i in range(10)}
		for numberSet in powerset(range(1, 10)):
			size = len(numberSet)
			total = sum(numberSet)
			if total in self.possibleNumbers[size]:
				self.possibleNumbers[size][total].append(set(numberSet))
			else:
				self.possibleNumbers[size][total] = [set(numberSet)]

	def possibleNumberSets(self, numberOfNumbers, desiredSum):
		if desiredSum not in self.possibleNumbers[numberOfNumbers]:
			return set()
		return self.possibleNumbers[numberOfNumbers][desiredSum]

class SumConstraint:

	def __init__(self, indexList, requiredSum):
		'''
		indexList is a list of ordered pairs of indices. They must sum to the desired (cryptic) sum.
		'''
		self.requiredSum = requiredSum
		self.indexList = indexList

	def __str__(self):
		return str(self.indexList) + ' sum to ' + str(self.requiredSum)

	def __repr__(self):
		return str(self)

class CrypticKakuro:

	def __init__(self, textDescription):
		'''
		Takes in a text description of a cryptic kakuro board as given by those on PE 424 website and sets up
		the board state
		'''
		self.puzzleSize = int(textDescription[0])
		puzzleElements = [box for box in self.splitByBoxes(textDescription[2:])]

		self.board = [['X' for i in range(self.puzzleSize)] for j in range(self.puzzleSize)]
		for serialIndex in range(len(puzzleElements)):
			col = serialIndex % self.puzzleSize
			row = serialIndex / self.puzzleSize
			self.board[row][col] = puzzleElements[serialIndex]

		self.indexPairToConstraints = {(i, j) : [] for (i, j) in product(range(len(self.board)), repeat=2)}
		self.sumConstraints = []
		
		for rowIndex in range(len(self.board)):
			for colIndex in range(len(self.board[rowIndex])):
				if self.boxIsConstraint(self.board[rowIndex][colIndex]):
					constraints = self.board[rowIndex][colIndex]
					self.board[rowIndex][colIndex] = 'X'
					self.addConstraints(rowIndex, colIndex, constraints[1:-1].split(','))

	def boxIsConstraint(self, boxValue):
		return boxValue[0] == '(' and boxValue[-1] == ')'

	def boxIsFillable(self, boxValue):
		return boxValue == 'O' or boxValue in [chr(i) for i in range(ord('A'), ord('K'))]

	def addConstraints(self, rowIndex, colIndex, constraints):
		for constraint in constraints:
			self.addConstraint(rowIndex, colIndex, constraint)

	def addConstraint(self, rowIndex, colIndex, boxValue):
		affectedIndices = []
		direction = boxValue[0]
		requiredSum = boxValue[1:]
		if direction == 'v':
			rowIndexDelta = 1
			colIndexDelta = 0
		else:
			rowIndexDelta = 0
			colIndexDelta = 1
		i = rowIndex + rowIndexDelta
		j = colIndex + colIndexDelta
		while i < len(self.board) and j < len(self.board[i]) and self.boxIsFillable(self.board[i][j]):
			affectedIndices.append((i,j))
			i += rowIndexDelta
			j += colIndexDelta
		constraint = SumConstraint(affectedIndices, requiredSum)
		self.sumConstraints.append(constraint)

		for indexPair in affectedIndices:
			if indexPair in self.indexPairToConstraints:
				self.indexPairToConstraints[indexPair].append(constraint)



	def splitByBoxes(self, textDescription):
		'''
		Can't do a simple string.split() on the input text description because vertical/horizontal information is recorded with a comma.
		'''
		numParens = 0
		lastIndex = 0
		for index in range(len(textDescription)):
			if textDescription[index] == '(':
				numParens += 1
			elif textDescription[index] == ')':
				numParens -= 1
			elif textDescription[index] == ',' and numParens == 0:
				yield textDescription[lastIndex : index]
				lastIndex = index + 1
		yield textDescription[lastIndex : len(textDescription)]

	def getOpenSquareIndices(self):
		for rowIndex in range(len(self.board)):
			for colIndex in range(len(self.board[rowIndex])):
				if self.boxIsFillable(self.board[rowIndex][colIndex]):
					yield (rowIndex, colIndex)

	def getSumConstraints(self, rowIndex, colIndex):
		return self.indexPairToConstraints[(rowIndex, colIndex)]

	def __str__(self):
		return '\n'.join([''.join(row) for row in self.board])


class CrypticKakuroSolver:

	def __init__(self):
		#
		print 'initializing solver'
		self.sp = SumPossibilities()

	def solveCrypticKakuro(self, crypticKakuro):
		self.puzzle = crypticKakuro
		self.crypticKey = {chr(character) : [i for i in range(10)] for character in range(ord('A'), ord('K'))}
		self.indicesToNumbers = { openSquare : [i for i in range(1, 10)] for openSquare in crypticKakuro.getOpenSquareIndices()}
		self.deductionStack = []

		while not self.isSolved():

			self.debug = False
			self.madeDeduction = True
			self.foundContradiction = False
			# Try to do as much deduction as possible before brute forcing.
			while self.madeDeduction and not self.isSolved() and not self.foundContradiction:
				self.madeDeduction = False
				deducer_names = ['infer_letters_from_totals', 'infer_letters_by_exclusion', 'infer_squares_by_total',\
								'infer_squares_by_max', 'infer_squares_by_min', 'infer_squares_by_exclusion', 'unify_square_and_contained_letter']
				for method in deducer_names:
					if self.foundContradiction:
						break
					if hasattr(self, method):
						func = getattr(self, method)
						nargs = func.func_code.co_argcount-1
						if nargs:
							args = self.pop(nargs)
							if self.debug:
								logging.debug('exec: %s %r' % (name, args))
								if len(args) == nargs:
									func(*args)
						else:
							if self.debug:
								logging.debug('exec: %s' % name)
							func()
					else:
						raise NotImplementedError


			if self.foundContradiction or self.containsContradiction():
				# Pop stuff off the deduction stack until we come to the element that's a guess and then deduce that it cannot be that.
				self.foundContradiction = False
				# print self.crypticKey
				while self.deductionStack[-1][3] == 'Deduction':
					restoration_tuple = self.deductionStack.pop()
					restore_func = restoration_tuple[0]
					restore_arg1 = restoration_tuple[1]
					restore_arg2 = restoration_tuple[2]
					restore_func(self, restore_arg1, restore_arg2)

				# Next item on the stack is a guess, so we pop it off and we're gucci.
				restoration_tuple = self.deductionStack.pop()

				restore_func = restoration_tuple[0]
				restore_arg1 = restoration_tuple[1]
				restore_arg2 = restoration_tuple[2]
				restore_func(self, restore_arg1, restore_arg2)
			
			elif not self.isSolved():
				# Partial brute force backtrack
				self.guess_best_option()

	def guess_best_option(self):
		# As a heuristic, use the option from cryptic key or square with the least number of possibilities
		minimum_letter_possibilities = 10
		minimum_letter = None
		minimum_square_possibilities = 11
		minimum_square = None
		for letter in self.crypticKey.keys():
			if 1 < len(self.crypticKey[letter]) < minimum_letter_possibilities:
				minimum_letter = letter
				minimum_letter_possibilities = len(self.crypticKey[letter])

		for index_pair in self.puzzle.getOpenSquareIndices():
			if 1 < len(self.indicesToNumbers[index_pair]) < minimum_square_possibilities:
				minimum_square = index_pair
				minimum_square_possibilities = len(self.indicesToNumbers[index_pair])

		if minimum_letter_possibilities < minimum_square_possibilities and minimum_letter is not None:
			self.guess_letter_must_be(minimum_letter, self.crypticKey[minimum_letter][0])
		elif minimum_square is not None:
			self.guess_square_must_be(minimum_square, self.indicesToNumbers[minimum_square][0])
		else:
			print self.crypticKey
			print self.indicesToNumbers
			print self.crypticKey['0']


	def guess_square_must_be(self, index_pair, number):
		original_possibilities = [i for i in self.indicesToNumbers[index_pair]]
		def restore_state(self, index_pair, number):
			self.indicesToNumbers[index_pair] = original_possibilities
			self.deduce_square_cannot_be(index_pair, number)
		
		if self.debug:
			print 'guessing %s is %s' %(index_pair, number)

		self.indicesToNumbers[index_pair] = [number]
		self.deductionStack.append((restore_state, index_pair, number, 'Guess'))

	def guess_letter_must_be(self, letter, number):
		original_possibilities = [i for i in self.crypticKey[letter]]
		def restore_state(self, letter, number):
			self.crypticKey[letter] = original_possibilities
			self.deduce_letter_cannot_be(letter, number)
	
		if self.debug:
			print 'guessing %s and %s' %(letter, number)
		self.crypticKey[letter] = [number]
		self.deductionStack.append((restore_state, letter, number, 'Guess'))


	def deduce_letter_cannot_be(self, letter, number):
		if number in self.crypticKey[letter]:
			self.madeDeduction = True

			self.crypticKey[letter].remove(number)
			if len(self.crypticKey[letter]) == 0:
				self.foundContradiction = True
			
			def undeduce_letter_cannot_be(self, letter, number):
				self.crypticKey[letter].append(number)

			self.deductionStack.append((undeduce_letter_cannot_be, letter, number, 'Deduction'))


	def deduce_square_cannot_be(self, index_pair, number):
		if number in self.indicesToNumbers[index_pair]:
			self.madeDeduction = True

			self.indicesToNumbers[index_pair].remove(number)
			if len(self.indicesToNumbers[index_pair]) == 0:
				self.foundContradiction = True
			def undeduce_square_cannot_be(self, index_pair, number):
				self.indicesToNumbers[index_pair].append(number)

			self.deductionStack.append((undeduce_square_cannot_be, index_pair, number, 'Deduction'))


	def deduce_square_must_be(self, index_pair, number):
		for alternative in self.indicesToNumbers[index_pair]:
			if alternative != number:
				self.deduce_square_cannot_be(index_pair, alternative)

	def deduce_letter_must_be(self, letter, number):
		for alternative in self.crypticKey[letter]:
			if alternative != number:
				self.deduce_letter_cannot_be(letter, number)

	def infer_letters_from_totals(self):
		two_totals = {i for i in xrange(3, 18)}
		three_totals = {i for i in xrange(6, 25)}
		four_totals = {i for i in xrange(10, 31)}
		five_totals = {i for i in xrange(15, 36)}
		six_totals = {i for i in xrange(21, 40)}
		if self.debug:
			print 'inferring letters from totals'
		mp_len_totals = {2 : two_totals, 3 : three_totals, 4 : four_totals, 5 : five_totals, 6 : six_totals}

		for constraint in self.puzzle.sumConstraints:
			possible_totals = {i for i in mp_len_totals[len(constraint.indexList)] if self.matchesPossibilities(str(i), constraint.requiredSum)}
			if len(constraint.requiredSum) == 2 and len(set(constraint.requiredSum)) == 1:
				possible_totals = {i for i in possible_totals if len(set(str(i))) == 1}

			for index, letter in enumerate(constraint.requiredSum):
				possible_letter_values = set()
				for possible_total in possible_totals:
					possible_letter_values.add(int(str(possible_total)[index]))
				
				impossible_letter_values = {i for i in range(10)} - possible_letter_values
				for number in impossible_letter_values:
					self.deduce_letter_cannot_be(letter, number)
					if self.foundContradiction:
						return

	def infer_letters_by_exclusion(self):
		if self.debug:
			print 'inferring letters by exclusion'
		for solved_letter in self.crypticKey.keys():
			if len(self.crypticKey[solved_letter]) == 1:
				for other_letter in self.crypticKey.keys():
					if other_letter != solved_letter:
						self.deduce_letter_cannot_be(other_letter, self.crypticKey[solved_letter][0])
						if self.foundContradiction:
							return

	def infer_squares_by_exclusion(self):
		if self.debug:
			print 'inferring squares by exclusion'
		for index_pair in self.puzzle.getOpenSquareIndices():
			if len(self.indicesToNumbers[index_pair]) == 1:
				excluded_number = self.indicesToNumbers[index_pair][0]
				for constraint in self.puzzle.indexPairToConstraints[index_pair]:
					for ij in constraint.indexList:
						if ij != index_pair:
							self.deduce_square_cannot_be(ij, excluded_number)


	def infer_squares_by_min(self):
		if self.debug:
			print 'inferring squares by their minimum possible values'
		for index_pair in self.puzzle.getOpenSquareIndices():
			squareConstraints = self.puzzle.indexPairToConstraints[index_pair]
			for constraint in squareConstraints:
				encoded_sum = constraint.requiredSum
				possible_decoded_sums = self.get_possible_decoded_sums(encoded_sum)
				minimum_decoded_sum = min(possible_decoded_sums)

				# minimum sum of all squares in this constraint besides the current one
				maximum_possible_other_sum = 0
				for ij in constraint.indexList:
					if ij != index_pair:
						maximum_possible_other_sum += max(self.indicesToNumbers[ij] or [9])
				min_possible_value = minimum_decoded_sum - maximum_possible_other_sum

				for impossible_value in range(1, min_possible_value):
					self.deduce_square_cannot_be(index_pair, impossible_value)

	def infer_squares_by_max(self):
		if self.debug:
			print 'inferring squares by their maximum possible values'
		for index_pair in self.puzzle.getOpenSquareIndices():
			squareConstraints = self.puzzle.indexPairToConstraints[index_pair]
			for constraint in squareConstraints:
				encoded_sum = constraint.requiredSum
				possible_decoded_sums = self.get_possible_decoded_sums(encoded_sum)
				maximum_decoded_sum = max(possible_decoded_sums)

				# minimum sum of all squares in this constraint besides the current one
				minimum_possible_other_sum = 0
				for ij in constraint.indexList:
					if ij != index_pair:
						minimum_possible_other_sum += min(self.indicesToNumbers[ij] or [0])
				max_possible_value = maximum_decoded_sum - minimum_possible_other_sum

				for impossible_value in range(max_possible_value + 1, 10):
					self.deduce_square_cannot_be(index_pair, impossible_value)
					if self.foundContradiction:
						return

	def infer_squares_by_total(self):
		if self.debug:
			print 'inferring squares by their (potentially) known totals'
		for index_pair in self.puzzle.getOpenSquareIndices():
			squareConstraints = self.puzzle.indexPairToConstraints[index_pair]
			for constraint in squareConstraints:
				encoded_sum = constraint.requiredSum
				possible_decoded_sums = self.get_possible_decoded_sums(encoded_sum)
				possible_square_values = set()
				for decoded_sum in possible_decoded_sums:
					for numberSet in self.sp.possibleNumberSets(len(constraint.indexList), decoded_sum):
						for number in numberSet:
							possible_square_values.add(number)

				impossible_square_values = {i for i in range(1, 10)} - possible_square_values
				for value in impossible_square_values:
					self.deduce_square_cannot_be(index_pair, value)
					if self.foundContradiction:
						return

	def unify_square_and_contained_letter(self):
		if self.debug:
			print 'unifying ruled out possibilities based on a square and letter being the same thing'
		for index_pair in self.puzzle.getOpenSquareIndices():
			i,j = index_pair
			if self.puzzle.board[i][j] in {chr(character) for character in range(ord('A'), ord('K'))}:
				letter = self.puzzle.board[i][j]
				letter_possibilities = set(self.crypticKey[letter])
				square_possibilities = set(self.indicesToNumbers[index_pair])
				common_possibilities = square_possibilities.intersection(letter_possibilities)
				for number in letter_possibilities - common_possibilities:
					self.deduce_letter_cannot_be(letter, number)
				for number in square_possibilities - common_possibilities:
					self.deduce_square_cannot_be(index_pair, number)

	def get_possible_decoded_sums(self, encoded_sum):
		''' idea is to use itertools product with all candidates'''
		nested = product(*[self.crypticKey[letter] for letter in encoded_sum])
		return [int(''.join([str(j) for j in i])) for i in nested]


	def matchesPossibilities(self, candidate, requiredSum):
		if len(candidate) != len(requiredSum):
			return False

		for (candidateNum, constraintNum) in zip(candidate, requiredSum):
			if int(candidateNum) not in self.crypticKey[constraintNum]:
				return False

		return True

	def containsContradiction(self):
		for rowIndex, colIndex in self.puzzle.getOpenSquareIndices():
			index_pair = (rowIndex, colIndex)

			if len(self.indicesToNumbers[index_pair]) == 1:
				deduced_number = self.indicesToNumbers[index_pair][0]
				if self.puzzle.board[rowIndex][colIndex] in {chr(character) for character in range(ord('A'), ord('K'))}:
					unified_letter = self.puzzle.board[rowIndex][colIndex]
					if deduced_number not in self.crypticKey[unified_letter]:
						return True

				for constraint in self.puzzle.getSumConstraints(rowIndex, colIndex):
					for other_indices in constraint.indexList:
						if other_indices != index_pair and len(self.indicesToNumbers[other_indices]) == 1 and self.indicesToNumbers[other_indices][0] == deduced_number:
							return True

					if all([len(self.indicesToNumbers[indices]) == 1 for indices in constraint.indexList]):
						actual_sum = sum([self.indicesToNumbers[indices][0] for indices in constraint.indexList])
						desired_sum = constraint.requiredSum
						if all([len(self.crypticKey[letter]) == 1 for letter in desired_sum]):
							trantab = self.getCurrentTranslationTable()
							decoded_desired_sum = int(desired_sum.translate(trantab))
							if actual_sum != decoded_desired_sum:
								return True

		return False

	def isSolved(self):

		# check all squares have exactly one value and this value matches any squares with explicitly set letter
		for rowIndex, colIndex in self.puzzle.getOpenSquareIndices():
			if len(self.indicesToNumbers[(rowIndex, colIndex)]) != 1:
				return False
				
			if self.puzzle.board[rowIndex][colIndex] in [chr(i) for i in range(ord('A'), ord('K'))]:
				requiredCharacter = self.puzzle.board[rowIndex][colIndex]
				if self.crypticKey[requiredCharacter][0] != self.indicesToNumbers[(rowIndex, colIndex)][0]:
					return False

		# check all cryptic keys have exactly one value
		for crypticValues in self.crypticKey.values():
			if len(crypticValues) > 1:
				return False

		# check all sum constraints are satisfied
		for sumConstraint in self.puzzle.sumConstraints:
			if not self.constraintIsSatisfied(sumConstraint):
				return False

		# check there's one of each cryptic value
		crypticValues = set([possibleValues[0] for possibleValues in self.crypticKey.values()])
		if len(crypticValues) < 10:
			return False

		return True

	def getCurrentTranslationTable(self):
		inAndOutTab = [(a, str(b[0])) for a,b in self.crypticKey.items() if len(b) == 1]
		intab = ''.join([inAndOutTab[i][0] for i in range(len(inAndOutTab))])
		outtab = ''.join([inAndOutTab[i][1] for i in range(len(inAndOutTab))])
		trantab = maketrans(intab, outtab)
		return trantab


	def constraintIsSatisfied(self, constraint):
		indices = constraint.indexList
		requiredSum = constraint.requiredSum
		assignedNumbers = [numberCandidates[0] for numberCandidates in map(lambda index : self.indicesToNumbers[index], indices)]
		trantab = self.getCurrentTranslationTable()
		try:
			decodedSum = int(requiredSum.translate(trantab))
		except ValueError:
			return False
		return sum(assignedNumbers) == decodedSum and len(assignedNumbers) == len(set(assignedNumbers))


 
sample_puzzle_descriptor = '6,X,X,(vCC),(vI),X,X,X,(hH),B,O,(vCA),(vJE),X,(hFE,vD),O,O,O,O,(hA),O,I,(hJC,vB),O,O,(hJC),H,O,O,O,X,X,X,(hJE),O,O,X'

puzzles = [line[:-1] for line in open('kakuro200.txt', 'r').readlines()]


total = 0
ckSolver = CrypticKakuroSolver()
for i, puzzle in enumerate(puzzles):
	ck = CrypticKakuro(puzzle)
	print 'solving puzzle %s, which looks like this: '%i
	print ck
	ckSolver.solveCrypticKakuro(ck)	
	items = sorted(ckSolver.crypticKey.items())
	total += int(''.join([str(item[1][0]) for item in items]))

	print 'solved puzzle %s' %i
	print 'Total after solving this puzzle is %s' % total

'''
Code takes a while to run, but does so correctly. It could be improved by adding more logical checks. I only have
barebones stuff right now. Result is very long, but last bit of it is:


Total after solving this puzzle is 1047221809524
solving puzzle 198, which looks like this: 
XXXXXXX
XXXXXOO
XXXXOOO
XXOOADX
XXOOOJX
XOOOXXX
XOAXXXX
solved puzzle 198
Total after solving this puzzle is 1050286937472
solving puzzle 199, which looks like this: 
XXXXXX
XOOXXX
XOOOIX
XXOAOX
XXHBFD
XXXXOC
solved puzzle 199
Total after solving this puzzle is 1059760019628
[Finished in 6454.5s]

'''
