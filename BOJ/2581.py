import sys
input = sys.stdin.readline

m = int(input())
n = int(input())

result = []
sumV = 0
minV = 10000
for i in range(n, m-1, -1):
    if i > 1:
        cnt = 0
        for j in range(2, i):
            if i % j == 0:
                cnt += 1
                break
        if cnt == 0:
            result.append(i)
            sumV += i
            minV = i

if len(result) == 0:
    print(-1)
else:
    print(sumV)
    print(minV)
