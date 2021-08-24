n, k = map(int, input().split())
list = []
for i in range(n):
    i = int(input())
    list.append(i)
list = list[::-1]
cnt = [0]*n
for i in range(len(list)):
    if k // list[i] != 0:
       cnt[i] += k//list[i]
       k -= cnt[i] * list[i]
print(sum(cnt))