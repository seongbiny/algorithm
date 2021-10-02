def inorder(n):
    global cnt
    # 배열이니까 배열크기 넘어가지 않도록
    if n <= N:
        # 왼쪽노드는 현재 인덱스의 2배
        inorder(n*2)
        # 더이상 못가면 값 넣기
        tree[n] = cnt
        # 값 넣었으면 증가시키기
        cnt += 1
        # 우측 노드는 인덱스 2배 + 1
        inorder(n*2+1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [0 for _ in range(N+1)]
    cnt = 1
    inorder(1)

    print(f'#{tc} {tree[1]} {tree[N//2]}')
