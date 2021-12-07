import math

n = int(input())

lst = []
sq = math.sqrt(n)

for i in range(1, int(sq)+1):
    if n % i == 0:
        lst.append(i)
        if n//i != i:
            lst.append(n//i)

lst.sort()
for j in range(len(lst)):
    print(lst[j], end=" ")