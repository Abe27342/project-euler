import numpy as np
import sympy
from fractions import Fraction

'''
For number 535, there are 4 states since 3 digits: have 0 digits, have 1 digit, have 2 digits, have 3 digits

the have 3 digits state is an absorber so we just say we're always gucci after that (oh that's clever it implicitly converts the sum I see)

0 digits -> 9/10 1/10 0
1 digit  -> 8/10 1/10 1/10
2 digits -> 9/10 0    0

'''

a = sympy.Matrix([[Fraction(1, 2), Fraction(1, 2)], [0, Fraction(1, 2)]])

def get_state_of_string(target_string, current_string):
	while not target_string.startswith(current_string):
		current_string = current_string[1:]
	return len(current_string)

def expected_num_steps(number_as_string):
	matrix_size = len(number_as_string)
	transient_matrix_values = []

	for state_i in range(matrix_size):
		row_i_counts = [0 for i in range(matrix_size)]
		for digit in range(10):
			state_index = get_state_of_string(number_as_string, number_as_string[:state_i] + str(digit))
			if state_index < matrix_size:
				row_i_counts[state_index] += 1
		transient_matrix_values.append([Fraction(count, 10) for count in row_i_counts])

	transient_matrix = sympy.Matrix(transient_matrix_values)
	inverse = (sympy.eye(matrix_size) - transient_matrix).inv()
	expected_end_of_run = np.sum(inverse[0,0:matrix_size])
	if not abs(expected_end_of_run - int(expected_end_of_run)) < 0.01:
		print expected_end_of_run - int(expected_end_of_run)

	return expected_end_of_run - matrix_size + 1 # the last part since k starts at the beginning of the run not the end.

total = 0
for n in range(2, 10**6):
	if n % 10**4 == 0:
		print n
	total += expected_num_steps(str(10**16 / n))

print total


