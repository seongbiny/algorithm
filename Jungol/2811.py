import math

lst = list(map(int, input().split()))

for i in lst:
    cnt = 0
    for j in range(1, int(math.sqrt(i))+1):
        if i == 1:
            cnt = 1
        elif i % j == 0:
            cnt += 2

    if cnt == 2:
        print("prime number")
    elif cnt >= 3:
        print("composite number")
    else:
        print("number one")