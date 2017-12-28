from helpers import memoize
'''
Number of beans is an invariant

center of mass of beans is an invariant

total energy of beans increases by 2 at each step


i.e. sum(m_i) = constant
     sum(m_i x_i) = constant
     sum(m_i x_i^2) increases by 2 for each move

     since a move takes two x_i's and increases one by one and decreases the other by 1.

     Note all m_i's are actually 1.

     what is the maximum energy state? according to simulation, final state is an array of ones with 0 or 1 hole
'''


@memoize
def t(i):
	if i == 0:
		return 123456
	else:
		t_prev = t(i - 1)
		if t_prev % 2 == 0:
			return t_prev / 2
		else:
			return (t_prev / 2) ^ 926252

@memoize
def b(i):
	return 1 + (t(i) % 2**11)

# Returns the sum of squares from 1 to n, inclusive
def sum_of_squares(n):
	return n * (n + 1) * (2 * n + 1) / 6

def num_steps_to_terminate(initial_state):
	center_of_mass = sum([index * initial_state[index] for index in range(len(initial_state))])
	initial_energy = sum([index * index * initial_state[index] for index in range(len(initial_state))])
	number_of_beans = sum(initial_state)
	ones_start = (2 * center_of_mass - number_of_beans * number_of_beans) / (2 * number_of_beans)
	
	hole = (2 * ones_start + number_of_beans) * (number_of_beans + 1) / 2 - center_of_mass
	final_energy = sum_of_squares(ones_start + number_of_beans) - sum_of_squares(ones_start - 1) - hole * hole
	print initial_energy, final_energy, ones_start, hole
	return (final_energy - initial_energy) / 2

l = [b(i) for i in range(1, 1501)]
print num_steps_to_terminate(l)
