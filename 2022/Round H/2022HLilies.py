# Kickstart 2022: Round H, Lilies

def minCoins(L):
    minim = L
    q = []
    q.append([1, 0, 1]) #(cost, annotated, tossed)
    while q:
        [cost, ann, toss] = q.pop()
        if toss == L and cost < minim:
            minim = cost
        if toss < L and cost < minim:
            q.append([cost + 1, ann, toss + 1])
            q.append([cost+2, ann, toss + ann])
            q.append([cost + 6, toss, toss*2])
    return minim

# I/O Code
num_cases = int(input())

for case in range(1, num_cases + 1):
    L = int(input())
    print('Case #{}: {}'.format(case, minCoins(L)))
