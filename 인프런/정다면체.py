n, m = map(int, input().split())
res = [0]*(n+m+1)

for i in range(1, n+1):
    for j in range(1, m+1):
        res[i+j] += 1

ans = max(res)
for k in range(len(res)):
    if res[k] == ans:
        print(k, end=' ')