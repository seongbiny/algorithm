I = int(input())
for i in range(1,I+1):
    L, U, X = map(int,input().split())

    if X < L:
        result = L-X
    elif L <= X <= U:
        result = 0
    else:
        result = -1

    print(f'#{i} {result}')
