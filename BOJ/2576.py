lst = [int(input()) for i in range(7)]

minv = 999
sumv = 0
for i in range(len(lst)):
    if lst[i] % 2 == 1:
        sumv += lst[i]
        if lst[i] < minv:
            minv = lst[i]
if sumv == 0:
    print(-1)
else:
    print(sumv)
    print(minv)