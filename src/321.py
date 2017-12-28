'''
Not hard to convince oneself that the number of moves required for n counters is (n + 1)^2 - 1.

Let a = n + 1. We want to find the values of a that allow integer solutions to

a^2 - 1 = k(k+1)/2
2a^2 - 2 = k^2 + k
8a^2 - 7 = (2k + 1)^2
let b = 2k + 1
we want to find integer solutions to
b^2 - 8a^2 = -7, where b is odd.


first few values of a *should* be 2, 4, 11, 23, 64.

Fundamental solution to b^2 - 8a^2 = 1 is (3, 1)
also (17, 6) and (99, 35)
Solution solving the norm -7 problem is (1, 1).

So solutions should be of the form


(1, 1) * (3, 1)^n

where multiplication is defined by
(a, b) * (c, d) + (ac + 8bd, ad + bc)


'''

def group_multiplication(g, h):
	return (g[0] * h[0] + 8 * g[1] * h[1], g[0] * h[1] + g[1] * h[0])

N = 40

required_norm_soln = (-1, 1)
fundamental_soln = (3, 1)
def compute_solutions(required_num_values, starting_solution):
	solns = []
	current_soln = starting_solution
	while len(solns) < required_num_values:
		current_soln = group_multiplication(current_soln, fundamental_soln)
		solns.append(current_soln[1] - 1)
	return solns 

a = compute_solutions(100, (-1, 1))
a.extend(compute_solutions(100, (1, 1)))
a = sorted(a)

print sum(a[:N])

