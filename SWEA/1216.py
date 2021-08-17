import sys
sys.stdin = open("input_회문2.txt","r")

T = 10
for tc in range(1, T+1):
    n = int(input())
    arr = [input() for _ in range(100)]
    result = 0
    newnewarr=[]
    cnt_row = [0] * 100
    # 가로축
    for i in range(100):
        for j in range(100):
            for k in range(1,99-j):
                if arr[i][j] == arr[i][j+k]:
                    if arr[i][j:j+k] == arr[i][j:j+k][::-1]:
                        cnt_row.append(k+1)
                        maxV = 0
                        if maxV < cnt_row[j]:
                            maxV = cnt_row[j]

    # 세로축
    cnt_col = [0] * 100
    for i in range(100):
        newarr = []
        for j in range(100):
            newarr += arr[j][i]
        newnewarr.append(''.join(newarr))
    #print(newnewarr)

    for i in range(100):
        for j in range(100):
            for k in range(1, 99-j):
                if newnewarr[i][j] == newnewarr[i][j+k]:
                    if newnewarr[i][j:j+k] == newnewarr[i][j:j+k][::-1]:
                        cnt_col.append(k+1)
                        max = 0
                        if max < cnt_col[j]:
                            max = cnt_col[j]
    if max <= maxV:
        result += maxV
    else:
        result += max

    print(f'#{tc} {result}')


