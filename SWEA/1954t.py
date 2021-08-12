T = int(input())
for tc in range(1, T+1):
    N = int(input())

    snail = [[0] * N for _ in range(N)]
    #방향전환 : 못채울때 + 이미 데이터가 채워져있을때
    #우, 하, 좌, 상, 우 ..
    dx = []
    dy = []
    #mode = 0, 1, 2, 3, 1, 2, 3, 0, 1, 2
    mode += 1
    if mode == 4:
        mode = 0

    mode = (mode + 1) % 4 # 자동으로 0123 0123 ...

    brd = [[0] * N for _ in range(N)]
    value = 1

    #좌표
    curr = 0
    curc = 0

    while value <= N**2:
        brd[curr][curc] = value
        #1. 좌표 갱신을 위하여 새로운 좌표가 유효한지 확인한다.
        newr = curr + dx[mode]
        newc = curc + dy[mode]
        #2. 좌표가 유효하지 않으면 방향전환 (행렬 크기를 벗어나거나, 원소가 0이 아닐때)
        if not (0 < newr <= N and 0 < newc <= N) or snail[newr][newc] != 0:
            mode = (mode + 1) & 4
        #3. 좌표를 갱신한다.
        curr = curr + dx[mode]
        curc = curc + dy[mode]
        value += 1
    print(snail)