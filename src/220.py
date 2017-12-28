'''
a -> aRbFR
b -> LFaLb


Some setup stuff to play around with the problem, then the actual solution. Runs very quickly--didn't even bother memoizing it, though this
would help for larger input.


'''



def D(n):
	if n == 0:
		return 'Fa'
	else:
		return D(n-1).replace('a', 'aRcFR').replace('b', 'LFaLb').replace('c', 'b')

class Dragon:

	def __init__(self, max_num_forwards = -1):
		self.x_dir = 0
		self.y_dir = 1
		self.x_pos = 0
		self.y_pos = 0
		self.max_num_forwards = max_num_forwards
		self.num_forwards = 0

	def consume_character(self, character):
		if self.num_forwards != self.max_num_forwards:
			if character == 'F':
				self.num_forwards += 1

				self.x_pos += self.x_dir
				self.y_pos += self.y_dir
			elif character == 'R':
				self.x_dir, self.y_dir = self.y_dir, -self.x_dir
			elif character == 'L':
				self.x_dir, self.y_dir = -self.y_dir, self.x_dir

	def consume_string(self, string):
		for character in string:
			self.consume_character(character)


def get_last_position(n):
	instructions = D(n)
	dragon = Dragon()

	dragon.consume_string(instructions)
	print dragon.num_forwards
	return (dragon.x_pos, dragon.y_pos)

print [get_last_position(i) for i in range(10)]

'''
Initial few end positions are:
(0, 1)
(1, 1)
(2, 0)
(2, -2)
(0, -4)
(-4, -4)
(-8, 0)
... and so on

spirals outward at theta = -45 degrees and radius sqrt(2)

so end position for k in the complex plane is 

z_k = i * (sqrt(2) cis(-i pi/4))^k
    = i * (sqrt(2) * (1/sqrt(2) - i/sqrt(2)))^n
    = i * (1 - i)^n
let a_k = re(z_k), b_k = im(z_k)

then a_0 = 0, b_0 = 1

z_n = (1 - i)(a_{n-1} + b_{n-1} i)
    = a_{n-1} + b_{n-1} + (b_{n-1} - a_{n-1}) i 

so a_n = a_{n-1} + b_{n-1} and b_n = b_{n-1} - a_{n-1}
'''

def end_position(k):
	if k == 0:
		return (0, 1)
	else:
		a, b = end_position(k - 1)
		return (a + b, b - a)


def position_after_n_steps_in_Dk(n, k):
	if k == 0:
		if n == 0:
			return (0, 0)
		assert n == 1
		return (0, 1)
	else:
		if n <= pow(2, k - 1):
			return position_after_n_steps_in_Dk(n, k - 1)
		else:
			x_first, y_first = end_position(k - 1)

			# Now get the offset from the end and rotate it.
			x_recursive, y_recursive = position_after_n_steps_in_Dk(pow(2, k) - n, k - 1)
			
			x_recursive -= x_first
			y_recursive -= y_first
			# Now we need to rotate the backward steps and add it to the initial steps.
			return (x_first - y_recursive, y_first + x_recursive)
print position_after_n_steps_in_Dk(10**12, 50)
# print position_after_n_steps_in_Dk(3, 3)
# print [position_after_n_steps_in_Dk(i, 4) for i in range(16)]
