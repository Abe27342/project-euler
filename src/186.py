''' Shameless copypasta from some random site. Union find me to victory :)'''

"""UnionFind.py

Union-find data structure. Based on Josiah Carlson's code,
http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/215912
with significant additional changes by D. Eppstein.
"""

class UnionFind:
    """Union-find data structure.

    Each unionFind instance X maintains a family of disjoint sets of
    hashable objects, supporting the following two methods:

    - X[item] returns a name for the set containing the given item.
      Each set is named by an arbitrarily-chosen one of its members; as
      long as the set remains unchanged it will keep the same name. If
      the item is not yet part of a set in X, a new singleton set is
      created for it.

    - X.union(item1, item2, ...) merges the sets containing each item
      into a single larger set.  If any item is not yet part of a set
      in X, it is added to X as one of the members of the merged set.
    """

    def __init__(self):
        """Create a new empty union-find structure."""
        self.weights = {}
        self.parents = {}

    def __getitem__(self, object):
        """Find and return the name of the set containing the object."""

        # check for previously unknown object
        if object not in self.parents:
            self.parents[object] = object
            self.weights[object] = 1
            return object

        # find path of objects leading to the root
        path = [object]
        root = self.parents[object]
        while root != path[-1]:
            path.append(root)
            root = self.parents[root]

        # compress the path and return
        for ancestor in path:
            self.parents[ancestor] = root
        return root
        
    def __iter__(self):
        """Iterate through all items ever found or unioned by this structure."""
        return iter(self.parents)

    def union(self, *objects):
        """Find the sets containing the objects and merge them all."""
        roots = [self[x] for x in objects]
        heaviest = max([(self.weights[r],r) for r in roots])[1]
        for r in roots:
            if r != heaviest:
                self.weights[heaviest] += self.weights[r]
                self.parents[r] = heaviest

uf = UnionFind()

prime_minister = 524287
modulus = 10 ** 6
for i in range(modulus):
   uf.union(i)
S = [(100003 - 200003 * k + 300007 * k * k * k) % modulus for k in range(56)]
current_call_number = 1



def get_caller_callee(call_number):
    while len(S) <= 2 * call_number:
        S.append((S[-24] + S[-55]) % modulus)
    return (S[2 * call_number - 1], S[2 * call_number])

call_number = 0
num_non_misdials = 0
while uf.weights[uf[prime_minister]] < 990000:
    call_number += 1
    caller, callee = get_caller_callee(call_number)
    if caller != callee:
        num_non_misdials += 1
        uf.union(caller, callee)

print num_non_misdials
