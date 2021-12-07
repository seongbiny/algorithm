import sys
input = sys.stdin.readline

t = int(input())
for tc in range(1, t+1):
    b, c = map(int, input().split())
    print(b+c)
