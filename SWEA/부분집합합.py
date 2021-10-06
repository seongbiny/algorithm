def prt():
    for i in range(N):
        if res[i] == 1:
            print(lst[i], end=' ')
    print()

def powerset(k, sumV):
    if sumV > 20:
        return
    if k == N:
        #print(res)
        # sumV = 0
        # for i in range(N):
        #     if res[i] == 1:
        #         sumV += lst[i]
        if sumV == 20:
            prt()
        return

    res[k] = 0
    powerset(k+1, sumV)

    res[k] = 1
    powerset(k+1, sumV+lst[k])

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
N = len(lst)
res = [-1] * N

powerset(0, 0)