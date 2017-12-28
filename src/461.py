from decimal import *
from math import floor
from itertools import combinations_with_replacement


''' Shameless copypasta from stack overflow '''
import os

def reverse_readline(filename):
    with open(filename) as qfile:
        qfile.seek(0, os.SEEK_END)
        position = qfile.tell()
        line = ''
        while position >= 0:
            qfile.seek(position)
            next_char = qfile.read(1)
            if next_char == "\n":
                yield line[::-1]
                line = ''
            else:
                line += next_char
            position -= 1
        yield line[::-1]

''' End shameless copypasta. '''



getcontext().prec = 20

desired_sum = Decimal('3.141592653589793238462643383')

n = 10000

nums = [(k, (Decimal(k) / Decimal(n)).exp() - 1) for k in range(1, int(floor(1.423 * n)))]

'''
list producted, now sorting list.
722643
list sorted, going through to find minimum now.
3.98432384626434E-11
(148, 398, 516, 1036)
1519860
[Finished in 93.8s]
'''

pairwise_sums_file = open('461/pairwise.txt', 'w')
for ((k1, k2), (k3, k4)) in combinations_with_replacement(nums, 2):
	if k2 + k4 < desired_sum:
		pairwise_sums_file.write('%s, %s, %s\n'%(k1, k3, k2 + k4))
pairwise_sums_file.close()
print 'list producted, now sorting list.'



def sorting_value(line):
	value = Decimal(line.split(',')[-1][:-1])
	return value

chunk_size = 10 ** 7
chunk_num = 0
pairwise_sums_file = open('461/pairwise.txt', 'r')
num_lines_current = 0
chunk_of_lines = []
current_temp_file = open('461/%s_temp.txt' % chunk_num, 'w')
for line in pairwise_sums_file:
	num_lines_current += 1
	chunk_of_lines.append(line)
	if num_lines_current == chunk_size:

		chunk_of_lines = sorted(chunk_of_lines, key = sorting_value)
		current_temp_file = open('461/%s_temp.txt' % chunk_num, 'w')
		for line in chunk_of_lines:
			current_temp_file.write(line)
		current_temp_file.close()

		chunk_of_lines = []
		num_lines_current = 0
		chunk_num += 1

chunk_of_lines = sorted(chunk_of_lines, key = sorting_value)
current_temp_file = open('461/%s_temp.txt' % chunk_num, 'w')
for line in chunk_of_lines:
	current_temp_file.write(line)
current_temp_file.close()

chunk_of_lines = []
num_lines_current = 0
chunk_num += 1

total_num_chunks = chunk_num

# Merge all files together to a single, sorted file.
list_of_files = [open('461/%s_temp.txt' % chunk, 'r') for chunk in range(total_num_chunks)]
sorted_pairwise_sum_file = open('461/sorted_pairwise_sum.txt', 'w')

while len(list_of_files) > 0:
	fp_with_min_line = None
	line_to_write = '1, 1, 10.0'
	fps_to_remove = []
	for fp in list_of_files:
		cur_pos = fp.tell()
		line = fp.readline()
		if line == '':
			fps_to_remove.append(fp)
			continue
		if sorting_value(line) < sorting_value(line_to_write):
			fp_with_min_line = fp
			line_to_write = line
		fp.seek(cur_pos)

	for fp in fps_to_remove:
		list_of_files.remove(fp)
	if fp_with_min_line is not None:
		fp_with_min_line.readline()
		sorted_pairwise_sum_file.write(line_to_write)

sorted_pairwise_sum_file.close()



min_error = 100
min_abcd = None

start_value = 0
end_value = 1

print 'list sorted, going through to find minimum now.'

forward_iterator = open('461/sorted_pairwise_sum.txt', 'r')
backward_iterator = reverse_readline('461/sorted_pairwise_sum.txt')
low_sum = 0
low_line = None
prev_low_line = None
prev_low_sum = 0
done = False
for high_line in backward_iterator:
	if high_line == '':
		continue
	high_sum = sorting_value(high_line)

	# For cases of going backwards, we had that the previous high_line was in [low_line, previous_low_line] and previous_low_line + high_line < desired < low_line + high_line.
	# Hence to consider all cases, we need to compare the current high_line with the previous two low lines to consider the cases where the high line is also in these intervals.
	# The while loop will only get triggered if the new high line happens to already be outside the interval.
	if low_line is not None:
		if abs(low_sum + high_sum - desired_sum) < min_error:
			min_error = abs(low_sum + high_sum - desired_sum)
			ab = [int(i) for i in low_line.split(',')[:2]]
			cd = [int(i) for i in high_line.split(',')[:2]]
			print ab, cd, abs(low_sum + high_sum - desired_sum)
			min_abcd = (ab[0], ab[1], cd[0], cd[1])

	if prev_low_line is not None:
		if abs(prev_low_sum + high_sum - desired_sum) < min_error:
			min_error = abs(prev_low_sum + high_sum - desired_sum)
			ab = [int(i) for i in prev_low_line.split(',')[:2]]
			cd = [int(i) for i in high_line.split(',')[:2]]
			print ab, cd, abs(prev_low_sum + high_sum - desired_sum)
			min_abcd = (ab[0], ab[1], cd[0], cd[1])
		

	while low_sum + high_sum < desired_sum:
		prev_low_line = low_line
		low_line = forward_iterator.readline()
		
		prev_low_sum = low_sum
		low_sum = sorting_value(low_line)

		if low_sum > high_sum:
			done = True
			break

		if abs(low_sum + high_sum - desired_sum) < min_error:
			min_error = abs(low_sum + high_sum - desired_sum)
			ab = [int(i) for i in low_line.split(',')[:2]]
			cd = [int(i) for i in high_line.split(',')[:2]]
			print ab, cd, abs(low_sum + high_sum - desired_sum)
			min_abcd = (ab[0], ab[1], cd[0], cd[1])
	if done or low_sum > high_sum:
		break

print min_error
print min_abcd
a,b,c,d = min_abcd
print a * a + b * b + c * c + d * d



'''
on precision 15:

[21, 106] [6570, 11631] 9.36761537356617E-13
[94, 244] [8074, 10527] 6.73238462643383E-13
[113, 373] [7084, 11189] 5.93238462643383E-13
[6, 560] [5793, 11935] 4.73238462643383E-13
[135, 622] [4475, 12526] 4.3238462643383E-14
[815, 871] [1780, 13273] 1.6761537356617E-14
[745, 1180] [6004, 11366] 3.238462643383E-15
3.238462643383E-15
(745, 1180, 6004, 11366)
167181397

'''



'''
on higher precision (20):

[94, 244] [8074, 10527] 6.42795462643383E-13
[113, 373] [7084, 11189] 5.76292662643383E-13
[6, 560] [5793, 11935] 4.40633162643383E-13
[135, 622] [4475, 12526] 4.8622462643383E-14
[363, 585] [668, 13801] 2.9116662643383E-14
[1332, 1404] [2382, 12752] 1.3890962643383E-14
[1433, 2147] [4903, 11363] 3.975762643383E-15
[1433, 4903] [2147, 11363] 3.975262643383E-15
3.975262643383E-15
(1433, 4903, 2147, 11363)
159820276
[Finished in 30170.7s]

holy shit that's 8.3 hours

'''