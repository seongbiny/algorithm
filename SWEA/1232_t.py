def calc(v):
    if len(tree[v]) == 2: # 피연산자라는 뜻
        return tree[v][1]
    else:
        L = calc(tree[v][2])
        R = calc(tree[v][3])

        if tree[v][1] == '+': return L+R
        elif tree[v][1] == '-': return L-R
        elif tree[v][1] == '*': return L*R
        elif tree[v][1] == '/': return L/R

for tc in range(1, 11):
    N = int(input()) # 정점의 개수
    tree = [0] * (N+1)

    for i in range(N):
        tmp = input().split()

        tree[int(tmp[0])] = tmp # 0번째는 정점 번호임

        # 먼저 처리를 하고 가자
        # tmp 길이가 4일 때, 0번 인덱스: 정점번호, 1번 인덱스: 연산자, 2번 인덱스: 왼자번, 3번 인덱스: 오자번
        if len(tmp) == 4:
            tree[int(tmp[0])][2] = int(tree[int(tmp[0])][2])
            tree[int(tmp[0])][3] = int(tree[int(tmp[0])][3])
        else:
            tree[int(tmp[0])][1] = int(tree[int(tmp[0])][1])

    print(f'#{tc} {int(calc(1))}')