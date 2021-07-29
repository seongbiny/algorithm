#0 1 2 3 4 5 6 7 8 9

T = int(input())
for i in range(T):
    num = int(input())
    N = 0

    result = []
    while result != list(range(1,10)):
        #result.append(num)
        N += 1
        num = num * N
        result.append(map(int,str(num)))

    print(f'#{T} {N}')
