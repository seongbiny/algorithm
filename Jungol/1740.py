import math

def prime(a):
    cnt = 0
    for j in range(1, int(math.sqrt(a))+1):
        if i == 1:
            continue
        elif a % j == 0:
            cnt += 2
    if cnt == 2:
        return True

m = int(input())
n = int(input())
sumv = 0
minv = 999999
for i in range(m, n+1):
    if prime(i) == True:
        sumv += i
        if minv > i:
            minv = i

if sumv == 0:
    print(-1)
else:
    print(sumv)
    print(minv)

