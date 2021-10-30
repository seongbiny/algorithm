def solve(lst, k):
    global j
    if k == N:
        # print(' '.join(list(map(str, lst))))
        j += 1
    elif j == lst[1]:
        print(' '.join(list(map(str, lst))))
    else:
        for i in range(1, N+1): # 1 2 3
            if i not in lst:
                solve(lst+[i], k+1)

import sys
input = sys.stdin.readline

N = int(input())
# lst = list(map(int, input().split()))
k, *lst = map(int, input().split())

if lst[0] == 1:
    j = 0
    solve([], 0)
elif lst[0] == 2:
    pass