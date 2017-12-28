



def right_rotate(n):
	a = str(n)
	return int(a[-1] + a[:-1])


l = [i for i in range(10, 10**6) if right_rotate(i) % i == 0]
print l