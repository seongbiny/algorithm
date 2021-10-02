import sys

N = int(input())
result = [0 for _ in range(10001)]
num = []

for i in range(N):
    num = int(sys.stdin.readline())
    result[num] += 1

for i in range(len(result)): # 0 1 2 3 4
    for j in range(result[i]): #
        print(i)
