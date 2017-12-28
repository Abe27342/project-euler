'''

First, a simulation...


Evidently, floor 1 contains all triangular numbers.
Looking on oeis,...
floor 2 contains numbers 2, 7, 9, 16 and then a(n) = 2a(n-1) - 2a(n-3) + a(n-4)
a(1) = 2
a(2) = 7
a(3) = 9
a(4) = 16

floor 3 contains a(0) = 1 then a(n) = n^2 - a(n-1) for n >= 1.
floor 4 contains blah blah blah

it turns out that P(f, r) is something like (r + f)(r + f - 1)/2 + f/2 * (-1)^(r + f).
This formula works for even f, and then for odd ones you have to modify it slightly. Should be evident by the simulation.

Why it works, I have no idea.

Also note that the given number is 2^27 * 3^12. That's how we arrive at the answer.
'''
from collections import defaultdict
from random import randint

squares = {i**2 for i in range(10000)}
def is_square(n):
	return n in squares

class Hotel:

	def __init__(self):
		self.floors = defaultdict(list)
		self.next_person_num = 1

	def try_place_in_floor(self, person_num, floor_num):
		floor = self.floors[floor_num]
		if len(floor) == 0:
			floor.append(person_num)
			return True
		else:
			last_person = floor[-1]
			if is_square(last_person + person_num):
				floor.append(person_num)
				return True
		return False


	def place_person(self, person_num):
		floor_num = 1
		while not self.try_place_in_floor(person_num, floor_num):
			floor_num += 1

	def place_next_person(self):
		self.place_person(self.next_person_num)
		self.next_person_num += 1


hotel = Hotel()

def P(f, r):
	while not (f in hotel.floors and r-1 < len(hotel.floors[f])):
		hotel.place_next_person()
	return hotel.floors[f][r - 1]


def fast_P(f, r):
	if f == 1:
		return r * (r + 1) / 2
	negative_one_coeff = f / 2
	negative_one_power = r + (f % 2)

	a1 = f - (f % 2)
	a2 = a1 - 1
	return (r + a1) * (r + a2) / 2 + negative_one_coeff * (-1)**(negative_one_power)
'''
print P(25, 75)
hotel.floors[1] = 0
hotel.floors[2] = 0
hotel.floors[3] = 0
hotel.floors[4] = 0
hotel.floors[5] = 0
print hotel.floors
print [fast_P(11, i) for i in range(1, 5)]
print hotel.floors[11]

experimentation
'''

def try_random_sample_case():
	f = randint(40, 150)
	r = randint(100, 200)
	assert P(f, r) == fast_P(f, r)

for i in range(1000):
	try_random_sample_case()

print [fast_P(1, i) for i in range(1, 101)]
print [P(1, i) for i in range(1, 101)]

n = 2**27 * 3**12
print n

total = 0
for p2 in range(28):
	for p3 in range(13):
		d = 2**p2 * 3**p3
		n_over_d = n / d
		total += fast_P(n_over_d, d)
		total %= 10**8

print total