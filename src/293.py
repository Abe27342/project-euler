from helpers import isPrimeMR

limit = 10**9
''' Awful, but it works.'''

def pseudofortunate(n):
	count = 2
	while not isPrimeMR(n + count):
		count += 1
	return count

def f(n):
	if n >= limit:
		return 0
	return pseudofortunate(n)

total = set()
for p2 in range(1, 31):
	num2 = pow(2, p2)
	total.add(f(num2))

	for p3 in range(1, 19):
		num3 = num2 * pow(3, p3)
		total.add(f(num3))
		if num3 > limit:
			break

		for p5 in range(1, 12):
			num5 = num3 * pow(5, p5)
			total.add(f(num5))
			if num5 > limit:
				break

			for p7 in range(1, 9):
				num7 = num5 * pow(7, p7)
				total.add(f(num7))
				if num7 > limit:
					break

				for p11 in range(1, 7):
					num11 = num7 * pow(11, p11)
					total.add(f(num11))
					if num11 > limit:
						break

					for p13 in range(1, 6):
						num13 = num11 * pow(13, p13)
						total.add(f(num13))
						if num13 > limit:
							break

						for p17 in range(1, 4):
							num17 = num13 * pow(17, p17)
							total.add(f(num17))
							if num17 > limit:
								break

							for p19 in range(1, 3):
								num19 = num17 * pow(19, p19)
								total.add(f(num19))
								if num19 > limit:
									break

								for p23 in range(1, 2):
									num23 = num19 * pow(23, p13)
									total.add(f(num23))

print sum(total)