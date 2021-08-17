def isFind(col):
    curr = 0
    curc = col
    while():
        if 왼쪽에 길이 있으면: #영역을 벗어나도 안되고 내가 가던 방향인지도
            d = -1
            curc = -1
        elif 오른쪽에 길이 있으면:
            d = 1
            curc += 1
        else:
            curr += 1

    if brd[curr][curc] == 2:
        return True
    else:
        return False

for i in range(100):
    if brd[0][i] == 1:
        #result = isFind(i) # 함수만들어
        if isFind(i): #result: #트루이면
            result = i
            break


print(f'#{tc} {result}')