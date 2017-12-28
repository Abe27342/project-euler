from helpers import sieve
from collections import deque

N = 10 ** 7

class Vertex:

	def __init__(self, n):
		self.n = n
		self.isVisited = False
		self.min_chain_type_checked = N
		self.adjacentVertices = set()

	def addAdjacentVertex(self, otherVertex):
		self.adjacentVertices.add(otherVertex)

primes = sieve(N)

# to make lookup easy.
setprimes = set(primes)
vertices = {p : Vertex(p) for p in primes}

def getConnectedNumbers(prime, max_num):
	for digit in range(1, 10):
		candidate = int(str(digit) + str(prime))
		if candidate in setprimes and candidate < max_num and candidate != prime:
			yield candidate

	#for digit in range(10):
	#	candidate = int(str(prime) + str(digit))
	#	if candidate in setprimes and candidate < max_num and candidate != prime:
	#		yield candidate

	for position in range(len(str(prime))):
		current_digit = str(prime)[position]
		# including 0 covers the case where we chop off the first digit for position 0.
		for new_digit in range(10):
			candidate = [i for i in str(prime)]
			candidate[position] = str(new_digit)
			if len(candidate) > 1 and candidate[0] == candidate[1] == '0':
				continue
			candidate = int(''.join(candidate))
			if candidate in setprimes and candidate < max_num and candidate != prime:
				yield candidate
	#candidate = prime / 10
	#if candidate in setprimes and candidate < max_num and candidate != prime:
	#	yield candidate


for prime in primes:
	vertex = vertices[prime]
	for connection in getConnectedNumbers(prime, N):
		vertices[connection].addAdjacentVertex(vertex)

print 'about to start queue time baby'

stack = deque([(0, vertices[2])])
while len(stack) > 0:
	min_valid_chain_num,currentVertex = stack.popleft()
	# print min_valid_chain_num, currentVertex.n
	if min_valid_chain_num <= currentVertex.n:
		# we've found a valid chain from 2 to this number, so we can say it's visited.
		currentVertex.isVisited = True

	for adjacentVertex in currentVertex.adjacentVertices:
		if not adjacentVertex.isVisited:
			k = max(min_valid_chain_num, currentVertex.n)
			if k < adjacentVertex.min_chain_type_checked:
				adjacentVertex.min_chain_type_checked = k
				stack.append((k, adjacentVertex))

print sum([p for p in primes if not vertices[p].isVisited])

#print 'computed'
# print [vertex.n for vertex in vertices[2207].adjacentVertices]

#print len(primes)