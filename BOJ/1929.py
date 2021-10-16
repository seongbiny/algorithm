M, N = map(int, input().split())

for i in range(M, N+1):
    a = 0
    for j in range(2, i):
        if i % j == 0:
            a += 1
    if a == 0 and i % i == 0:
        print(i)

