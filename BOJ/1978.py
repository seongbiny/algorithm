import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))


result = 0
for i in arr:
    cnt = 0
    for j in range(1, i+1):
        if i % j == 0:
            cnt += 1
    if cnt == 2:
        result += 1

print(result)