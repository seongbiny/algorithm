def solve(lst, k):
    if k == N:
        print(' '.join(list(map(str, lst))))
    else:
        for i in range(1, N+1): # 1 2 3
            if i not in lst:
                solve(lst+[i], k+1)

N = int(input())
solve([],0)
