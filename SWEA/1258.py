T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    x_lst = []
    y_lst = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0:
                x_lst.append(i)
                y_lst.append(j)





