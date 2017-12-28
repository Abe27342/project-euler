from decimal import *
from math import floor
from itertools import combinations_with_replacement


''' Shameless copypasta from stack overflow '''
import os

class BackwardIterator:

	def __init__(self, filename):
		self.qfile = open(filename, 'r')
        self.qfile.seek(0, os.SEEK_END)
        self.position = qfile.tell()
        self.line = ''
        
    def readline(self):
        if self.position >= 0:
            self.qfile.seek(position)
            next_char = self.qfile.read(1)
            if next_char == "\n":
                return self.line[::-1]
                self.line = ''
            else:
                self.line += next_char
            self.position -= 1
        else:
	        return line[::-1]

	def close(self):
		self.qfile.close()

def reverse_readline(filename):
	return BackwardIterator(filename)
    


min_error = 100
min_abcd = None

start_value = 0
end_value = 1

print 'list sorted, going through to find minimum now.'

forward_iterator = open('461/sorted_pairwise_sum.txt', 'r')
backward_iterator = reverse_readline('461/sorted_pairwise_sum.txt')
low_sum = 0
low_line = foward_iterator.readline()
high_line = backward_iterator.readline()
prev_low_line = None
prev_low_sum = 0
done = False
while forward_iterator.tell() < backward_iterator.tell():
	if high_line == '':
		continue
	high_sum = sorting_value(high_line)
	low_sum = sorting_value(low_line)		
		
	if abs(low_sum + high_sum - desired_sum) < min_error:
		min_error = abs(low_sum + high_sum - desired_sum)
		ab = [int(i) for i in low_line.split(',')[:2]]
		cd = [int(i) for i in high_line.split(',')[:2]]
		print ab, cd, abs(low_sum + high_sum - desired_sum)
		min_abcd = (ab[0], ab[1], cd[0], cd[1])
	
	if low_sum + high_sum < desired_sum:
		low_line = forward_iterator.readline()
	else:
		high_line = backward_iterator.readline()

forward_iterator.close()
backward_iterator.close()

print min_error
print min_abcd
a,b,c,d = min_abcd
print a * a + b * b + c * c + d * d