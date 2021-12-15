import sys
input = sys.stdin.readline

a, b = map(int, input().split())

arr = []
for i in range(1, 50):
    for j in range(i):
        arr.append(i)
sumV = 0
for i in range(a-1, b):
    sumV += arr[i]

print(sumV)