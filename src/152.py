from fractions import Fraction


limit = 80
target = Fraction(1, 100)


potential_nums = range(2, limit + 1)

cumsum_from_end = 0
cumsums_from_end = {}
for i in range(limit, 1, -1):
	cumsum_from_end += Fraction(1, i * i)
	cumsums_from_end[i] = cumsum_from_end

# target = cumsums_from_end[2] - target



def num_ways(current_sum, min_index, current_nums):
	if current_sum == target:
		return 1
	elif current_sum + Fraction(1, limit * limit) > target:
		return 0
	elif min_index > 0 and current_sum + cumsums_from_end[potential_nums[min_index]] < target:
		return 0 
	else:
		total = 0
		print current_nums
		for new_min_index in range(min_index + 1, len(potential_nums)):
			next_num = potential_nums[new_min_index]
			current_nums.append(next_num)
			total += num_ways(current_sum + Fraction(1, next_num * next_num), new_min_index, current_nums) 
			current_nums.pop()
		return total

print target
print float(target)
print float(cumsums_from_end[limit / 2])
print num_ways(0, -1, [])