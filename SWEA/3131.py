# 2,3,5,7,

for i in range(2, 10**6+1):
    cnt = 0
    for j in range(2, i+1):
        if i % j == 0:
            cnt += 1
    if cnt == 1:
        print(i, end=' ')
