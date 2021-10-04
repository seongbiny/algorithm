T = int(input())
for tc in range(1, T+1):
    H, W = map(int, input().split())
    arr = [list(input()) for _ in range(H)]

    # [['*', '*', '*', '.', '.', '.', '.'],
    #  ['*', '-', '.', '.', '#', '*', '*'],
    #  ['#', '<', '.', '*', '*', '*', '*']]

    N = int(input())
    user_input = list(input())

    # S U R S S S S U S L S R S S S U R R D S R D S
    direction = ['^', 'v', '<', '>']
    dy = [0, 0, -1, 1]
    dx = [-1, 1, 0, 0]

    # 출발지점 찾기
    x, y = 0, 0
    for i in range(H):
        for j in range(W):
            if arr[i][j] in ['<', 'v', '^', '>']:
                x = i
                y = j
    # 명령어 실행
    for i in range(N):
        if user_input[i] == 'S':
            if arr[x][y] == '^':
                k = 0
            elif arr[x][y] == 'v':
                k = 1
            elif arr[x][y] == '<':
                k = 2
            elif arr[x][y] == '>':
                k = 3
            next_x = x + dx[k]
            next_y = y + dy[k]
            while 0 <= next_x < H and 0 <= next_y < W:
                if arr[next_x][next_y] == '#':
                    break
                elif arr[next_x][next_y] == '*':
                    arr[next_x][next_y] = '.'
                    break
                next_x += dx[k]
                next_y += dy[k]
        else:
            if user_input[i] == 'U':
                k = 0
            elif user_input[i] == 'D':
                k = 1
            elif user_input[i] == 'L':
                k = 2
            elif user_input[i] == 'R':
                k = 3
            if 0 <= x + dx[k] < H and 0 <= y + dy[k] < W and arr[x+dx[k]][y+dy[k]] == '.':
                arr[x][y] = '.'
                x += dx[k]
                y += dy[k]
            arr[x][y] = direction[k]

    print(f'#{tc}', end=' ')
    for i in range(H):
        print(''.join(arr[i]))
