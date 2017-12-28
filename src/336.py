

# returns the maximix arrangements for L train cars where L is a list of the train car names. 
def maximix_arrangements(L):
	L = sorted(L)
	if len(L) == 4:
		yield [L[3], L[0], L[2], L[1]]
		yield [L[3], L[1], L[0], L[2]]
		return 
	car_A = L[0]
	for arrangement in maximix_arrangements(L[1:]):
		for first_elem_of_end in range(1, len(arrangement)):
			first_part = arrangement[first_elem_of_end:]
			first_part.reverse()
			first_part.append(car_A)
			first_part.extend(arrangement[:first_elem_of_end])
			yield first_part

m = [''.join(i) for i in maximix_arrangements("ABCDEFGHIJK")]
print 'found the list!'
m = sorted(m)
print m[2010]