n, x = map(int, input().split())
lst = list(map(int, input().split()))
for i in range(n):
    if x > lst[i]:
        print(lst[i], end=' ')
