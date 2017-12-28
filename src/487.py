# Really fucking shitty problem.




# Returns the nth bernoulli number "mod p"
# in the sense that rational numbers are taken to be their inverses mod p.
bernoulli_memo = {}
def B(n, p):
	if (n,p) in bernoulli_memo:
		return bernoulli_memo[(n, p)]
	if n == 0:
		answer = 1
	else:
		answer = 0
	
	nchoosek = 1
	for k in range(n):
		sum_element = nchoosek * B(k, p) * pow(n - k + 1, -1, p)
		nchoosek = (n - k) * pow(k + 1, -1, p) * nchoosek
		answer -= sum_element
	
	bernoulli_memo[(n,p)] = answer
	return answer


