import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    arr = list(map(int, input().split()))

    arr.sort()
    print(arr[-3])