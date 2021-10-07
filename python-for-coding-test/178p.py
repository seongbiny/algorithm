N = int(input())
lst = []
for i in range(N):
    lst.append(int(input()))

lst = sorted(lst, reverse=True)

for i in range(N):
    print(lst[i], end=' ')