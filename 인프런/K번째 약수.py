n, k = map(int, input().split())
lst = [1,n]
for i in range(2, n):
    if n%i == 0:
        lst.append(i)
lst.sort()
if len(lst) >= k-1:
    print(lst[k-1])
else:
    print(-1)