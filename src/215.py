



def layers_of_length(n):
	if n < 2:
		return
	elif n == 2:
		yield [2]
	elif n == 3:
		yield [3]
	else:
		for layer in layers_of_length(n - 2):
			new_layer = [i for i in layer]
			new_layer.append(2)
			yield new_layer
		for layer in layers_of_length(n - 3):
			new_layer = [i for i in layer]
			new_layer.append(3)
			yield new_layer
			
layer_width = 32
num_layers = 10

layer_options = [tuple(i) for i in layers_of_length(layer_width)]

def cumulative_crack_positions(layer):
	crack = 0
	crack_positions = set()
	for brick_size in layer:
		crack += brick_size
		crack_positions.add(crack)

	crack_positions.remove(layer_width)
	return crack_positions


def has_no_crack(low_layer, high_layer):
	lower_cracks = cumulative_crack_positions(low_layer)
	higher_cracks = cumulative_crack_positions(high_layer)
	return lower_cracks.intersection(higher_cracks) == set()

previous_layer_counts = {i : 1 for i in layer_options}
current_layer_num = 1
while current_layer_num < num_layers:
	current_layer_num += 1
	print current_layer_num
	current_layer_counts = {i : 0 for i in layer_options}

	for current_layer in layer_options:
		for potential_prev_layer in layer_options:
			if has_no_crack(current_layer, potential_prev_layer):
				current_layer_counts[current_layer] += previous_layer_counts[potential_prev_layer] 

	previous_layer_counts = current_layer_counts

print sum(previous_layer_counts.values())