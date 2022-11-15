# Kickstart 2022: Round G, Walktober

def walk(others, john, N):
    s = 0
    for i in range(N):
        m = 0
        for j in range(len(others)):
            m = max(m, others[j][i])
        if m > john[i]:
            s += m-john[i]
    return s

# I/O Code
num_cases = int(input())

for case in range(1, num_cases + 1):
    [M, N, P] = list(map(int, input().split( )))
    others = []
    for m in range(M):
        if m == P-1:
            john = (list(map(int, input().split( ))))
        else:
            others.append(list(map(int, input().split( ))))
    print('Case #{}: {}'.format(case, walk(others, john, N)))
