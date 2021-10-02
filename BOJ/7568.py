n = int(input())
lst = [[] for _ in range(n)]

for i in range(n):
    lst[i] = list(map(int, input().split()))

for i in range(n): # 0 1 2 3
    cnt = 1
    for j in range(n): # 0 1 2 3
        if lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]:
            cnt += 1
    lst[i].append(cnt)

for i in range(len(lst)):
    print(lst[i][-1], end=' ')
