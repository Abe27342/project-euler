# (0,0) is bottom_left

# Because I'm too lazy to precompute lmao
from helpers import memoize

@memoize
def get_pow_2(n):
	return pow(2, n)

def is_top_left(N, bottom_right):
	x,y = bottom_right
	return x < get_pow_2(N - 1) and y >= get_pow_2(N - 1)

def is_bottom_left(N, top_right):
	x,y = top_right
	return x < get_pow_2(N - 1) and y < get_pow_2(N - 1)

def is_bottom_right(N, top_left):
	x,y = top_left
	return x >= get_pow_2(N - 1) and y < get_pow_2(N - 1)

def is_top_right(N, bottom_left):
	x,y = bottom_left 
	return x >= get_pow_2(N - 1) and y >= get_pow_2(N - 1)

def square_is_black(N, square):
	x,y = square
	middle = get_pow_2(N - 1)
	return (x - middle) * (x - middle) + (y - middle) * (y - middle) <= middle * middle

# Returns the encoding length for block with the given top_left and bottom_right corners in the 2^N by 2^N image.
def encoding_length(N, top_left, bottom_right):
	x_left, y_top = top_left 
	x_right, y_bottom = bottom_right 
	bottom_left = (x_left, y_bottom)
	top_right = (x_right, y_top)

	if is_top_left(N, bottom_right):
		if not square_is_black(N, bottom_right):
			return 2 # because 11 encoding gets all of the white parts.
		if square_is_black(N, bottom_right) and square_is_black(N, top_left):
			return 2
	elif is_top_right(N, bottom_left):
		if not square_is_black(N, bottom_left):
			return 2
		if square_is_black(N, bottom_left) and square_is_black(N, top_right):
			return 2
	elif is_bottom_left(N, top_right):
		if not square_is_black(N, top_right):
			return 2
		if square_is_black(N, bottom_left) and square_is_black(N, top_right):
			return 2
	elif is_bottom_right(N, top_left):
		if not square_is_black(N, top_left):
			return 2
		if square_is_black(N, bottom_right) and square_is_black(N, top_left):
			return 2

	current_square_size = y_top - y_bottom + 1 # Fuck this coordinate system :P
	if current_square_size == 1:
		return 2

	assert current_square_size % 2 == 0
	divided_size = current_square_size / 2
	top_left1 = top_left 
	top_left2 = (x_left + divided_size, y_top)
	top_left3 = (x_left, y_bottom + divided_size - 1)
	top_left4 = (x_left + divided_size, y_bottom + divided_size - 1)
	bottom_right1 = (x_left + divided_size - 1, y_bottom + divided_size)
	bottom_right2 = (x_right, y_bottom + divided_size)
	bottom_right3 = (x_left + divided_size - 1, y_bottom)
	bottom_right4 = bottom_right 
	return 1 + encoding_length(N, top_left1, bottom_right1) + encoding_length(N, top_left2, bottom_right2) + encoding_length(N, top_left3, bottom_right3) + encoding_length(N, top_left4, bottom_right4)

def D(N):
	return encoding_length(N, (0, pow(2, N) - 1), (pow(2, N) - 1, 0))

print [D(i) for i in range(2, 12)]
print D(24)