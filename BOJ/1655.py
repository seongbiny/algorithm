import sys
input = sys.stdin.readline

n = int(input())
lst = []
for i in range(1, n+1):
    lst.append(int(input()))
    lst.sort()
    #print(lst)

    if i % 2 != 0:
        print(lst[i//2])
    else:
        print(lst[i//2-1])
