import sys

N = int(sys.stdin.readline())
lst = [list(map(int,input().split())) for _ in range(N)]
lst.sort()
for i in range(len(lst)):
    print(lst[i][0], lst[i][1])

