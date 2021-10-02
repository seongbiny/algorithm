def preorder(N):
    global cnt
    if N > 0:
        cnt += 1
        preorder(tree[0][N])
        preorder(tree[1][N])

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))

    tree = [[0]*(E+2) for _ in range(2)]
    cnt = 0

    for i in range(E):
        n1, n2 = arr[i*2], arr[i*2+1]

        if tree[0][n1] == 0:
            tree[0][n1] = n2
        else:
            tree[1][n1] = n2

    preorder(N)
    print(f'#{tc} {cnt}')
