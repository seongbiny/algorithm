n = int(input())
lst = list(map(int, input().split()))
lst.sort()

if len(lst) == 1:
    print(lst[0]**2)
else:
    print(lst[0]*lst[-1])