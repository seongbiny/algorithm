T = 'Process finished with exit code 0'

def BM(P):
    M = len(P)
    N = len(T)

    SKIP = M * 128
    for i in range(M):
        #pos = ord(P[i])
        #SKIP[pos] = M-i-1
        SKIP[ord(P[i])] = M - i - 1

    idxT = 0
    while idxT <= N-M:
        idxP = M-1
        while idxP >= 0 and T[idxT + idxP] == P[idxP]:
            idxP -= 1
        if idxP == -1:
            return idxT
        pos = ord(T[idxT+M-1])
        idxT = idxT + SKIP[pos]

    return -1
