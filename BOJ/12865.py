import sys
input = sys.stdin.readline

n, k = map(int, input().split())
lst = []
for i in range(n):
    w, v = map(int, input().split())
    lst.append((w, v))

