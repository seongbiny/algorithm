T = int(input())
#    우, 하, 좌, 상   mode는 방향이다!!!!!
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
for tc in range(1, T+1):
    N = int(input())
    snail = [[0] * N for _ in range(N)]
    value = 1
    curr = 0
    curc = 0
    mode = 0
    while value <= N**2:
        #snail[curr][curc] = value
        if not snail[curc][curr]:
            snail[curc][curr] = value
        newr = curr + dx[mode]
        newc = curc + dy[mode]
        #value += 1
    #for value in range(1, (N**2)+1):
        #snail[curr][curc] = value

        #newr = curr + dx[mode]
        #newc = curc + dy[mode]

        if not (0 < curr <= N and 0 < curc <= N) or snail[curr][curc] != 0:
            mode = (mode + 1) & 4
        #value += 1
        #snail[newr][newc] = value
        curr = curr + dx[mode]
        curc = curc + dy[mode]

    print(snail)

