# Kickstart 2022: Round H, Lilies

def minCoins(L):
    minim = L
    ris = []
    q = []
    q.append([1, 0, 1, '']) #(cost, ann, toss, path)
    while q:
        [cost, ann, toss, path] = q.pop()
        if toss == L and cost < minim:
            minim = cost
            ris = [cost, ann, toss, path]
            #print(ris)
        if toss < L and cost < minim:
            q.append([cost + 1, ann, toss + 1, path + ' 1'])
            q.append([cost+2, ann, toss + ann, path + ' 2'])
            q.append([cost + 6, toss, toss*2, path + ' 4'])
    return minim

# I/O Code
num_cases = int(input())

for case in range(1, num_cases + 1):
    L = int(input())
    print('Case #{}: {}'.format(case, minCoins(L)))
