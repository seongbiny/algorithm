import math

n = int(input())
lst = []
for _ in range(n):
    lst.append(int(input()))


for i in lst:
    result = []
    for j in range(1, i+1):
        cnt = 0
        for k in range(1, int(math.sqrt(j))+1):
            if j % k == 0:
                cnt += 2
        if cnt == 2:
            result.append(j)

    num = i - result[-1]
    check = 0
    for j in range(1, int(math.sqrt(i+num+1))+1):
        if (i+num) % j == 0:
            check += 2
    if check == 2:
        print(result[-1], num+i)
    else:
        print(result[-1])