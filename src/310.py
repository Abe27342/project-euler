# answer: 2586528661783


N = 100000

nimbers = [0 for i in range(N + 1)]

for i in range(1, N + 1):
    possible_moves = {nimbers[i - j*j] for j in range(1, int(i**0.5) + 1)}
    i_nimber = 0
    while i_nimber in possible_moves:
        i_nimber += 1
    nimbers[i] = i_nimber

max_nimber = max(nimbers)

# nimber_count[(i, nimber)] is the number of nimbers with the value nimber
# at index i or greater.
nimber_count = {}
for nimber in range(max_nimber + 1):
    nimber_count[(0, nimber)] = nimbers.count(nimber)
for i in range(N):
    for nimber in range(max_nimber + 1):
        if nimber == nimbers[i]:
            nimber_count[(i + 1, nimber)] = nimber_count[(i, nimber)] - 1
        else:
            nimber_count[(i + 1, nimber)] = nimber_count[(i, nimber)]
print max_nimber
answer = 0
for a in range(N + 1):
    if a % 1000 == 0:
        print a
    for b in range(a, N + 1):
        if 0 <= nimbers[a] ^ nimbers[b] <= max_nimber:
            answer += nimber_count[(b, nimbers[a] ^ nimbers[b])]

print answer    

'''
Slow code to check correctness of above code for small cases.
answer = 0
for a in range(N + 1):
    for b in range(a, N + 1):
        for c in range(b, N + 1):
            if nimbers[a] ^ nimbers[b] ^ nimbers[c] == 0:
                answer += 1
print answer
'''
