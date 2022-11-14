# Kickstart 2022: Round H, Running

def lapCalc(l, n, lista):
    lap=0
    dirV = lista[0][1]
    kmEcc = 0
    for i in range(len(lista)):
        [unit, dir] = lista[i]
        if dir == dirV:
            unit += kmEcc
            lap += unit//l
            kmEcc = unit % l
        else:
            if unit > kmEcc:
                unit -= kmEcc
                dirV = dir
                lap += unit // l
                kmEcc = unit % l
            else:
                kmEcc -= unit
    return lap

# I/O Code
num_cases = int(input())

for case in range(1, num_cases + 1):
    mis = [int(d) for d in input().split()]
    L, N = mis[0], mis[1]
    lista = []
    for i in range(N):
        mis = [d for d in input().split( )]
        unit, dir = int(mis[0]), str(mis[1])
        lista.append([unit, dir])
    print('Case #{}: {}'.format(case, lapCalc(L, N, lista)))
