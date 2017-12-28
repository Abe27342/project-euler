from math import sqrt, sin, cos, atan2, pi, floor


def solve_quadratic(a, b, c):
	yield (-b + sqrt(b * b - 4 * a * c)) / (2 * a)
	yield (-b - sqrt(b * b - 4 * a * c)) / (2 * a)


def find_next_intersection_point(x0, y0, theta):
	return (-2 * y0 * sin(theta) - 8 * x0 * cos(theta))/(3 * cos(theta) * cos(theta) + 1)


# returns the angle of the normal line to (x0, y0) where 4x0^2 + y0^2 = 100
# evidently, 4x0 + y0 * y0' = 0, hence slope is (-y0)/(4x0). So atan2.
def normal_line_angle(x0, y0):
	return atan2(4 * x0, -y0) + pi / 2

def escapes(x, y):
	return -0.01 <= x <= 0.01 and y > 0

num_hits = 0
x0,y0 = 1.4,-9.6
theta = atan2(-19.7, 1.4)

theta = 2 * normal_line_angle(x0, y0) - theta
if cos(theta) > 0 and x0 > 0:
	theta = theta - pi
# print normal_line_angle(x0, y0)

while not escapes(x0, y0):
	num_hits += 1
	t = find_next_intersection_point(x0, y0, theta)
	x0 += t * cos(theta)
	y0 += t * sin(theta)

	theta = 2 * normal_line_angle(x0, y0) - theta
	if cos(theta) * x0 > 0:
		theta = theta - pi
	theta = theta - 2 * pi * floor(theta / (2 * pi))
	# print x0, y0, 180 * theta / pi

print num_hits
