n, k = map(int, input().split())
card = list(map(int, input().split()))
res=set()
# print(card)
plus = []
for i in range(n-2):
    for j in range(i+1,n-1):
        for m in range(j+1,n):
            res.add(card[i]+card[j]+card[m])
res = list(res)
res.sort(reverse=True)
print(res[k-1])


