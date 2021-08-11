arr[i][j]
    상: arr[i-1][i]
    하: arr[i+1][i]
    좌: arr[i][i-1]
    우: arr[i][i+1]

    #상하좌우
    dcol = [0, 0, -1, 1]
    drow = [-1, 1, 0, 0]

    상: arr[i+drow[0]][i+dcol[0]]
    하: arr[i+drow[1]][i+dcol[1]]
    좌: arr[i+drow[2]][i+dcol[2]]
    우: arr[i+drow[3]][j+dcol[3]]

    for mode in range(4):
        newrow = i +drow[mode]
        newcol = j +dcol[mode]
        print(arr[newrow][newcol])

for row in range(len(arr)):
    for col in range(len(arr[0])):
        for mode in range(4):
            newrow = row + drow[mode]
            newcol = col + dcol[mode]
            #if newrow, newcol 이 영역 안에 있을 때만:
            #    arr[newrow][newcol] 을 활용하여 값을 구한다.
            if 0 <= newrow < N and 0 <= newcol < M:
                arr[newrow][newcol]

dx = []
dy = []
for y in range(len(arr)):
    for x in range(len(arr[0])):
        for mode in range(4):
            newrow = y + dy[mode]
            newcol = x + dx[mode]