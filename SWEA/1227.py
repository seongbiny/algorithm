dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def solve(x, y):
    global cnt, end_x, end_y
    visited[x][y] = 1
    if x == end_x and y == end_y:
        cnt = 1
        return

    for d in range(4):
        new_x = x + dx[d]
        new_y = y + dy[d]

        if 0 <= new_x < 100 and 0 <= new_y < 100:
            if not visited[new_x][new_y] and arr[new_x][new_y] != 1:
                visited[new_x][new_y] = 1
                if arr[new_x][new_y] == 3:
                    cnt = 1
                solve(new_x, new_y)


for tc in range(1):
    arr = [list(map(int, input())) for _ in range(100)]
    visited = [[0] * 100 for _ in range(100)]
    cnt = 0

    for x in range(100):
        for y in range(100):
            if arr[x][y] == 2:
                start_x = x
                start_y = y
            elif arr[x][y] == 3:
                end_x = x
                end_y = y

    solve(start_x, start_y)
    print(f'#{tc} {cnt}')




