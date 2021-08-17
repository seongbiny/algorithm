def isCheck(str):
    #str이 회문이면 true
    #아니면 false를 return
    st = 0
    ed = len(str) - 1
    while st < ed and str[st] == str[ed]:
        st += 1
        ed -= 1
    if st >= ed:
        return True

    return False

def cc():
    #회문을 찾아서 return 하는 함수
    # 가로축
    for row in range(n):
        for st in range(0, n - m + 1):
            result = isCheck(arr[row][st:st + m])
            if result:
                return arr[row][st:st+m]

    # 세로축
    # 세로축은 슬라이싱 안돼 반복문으로 문자열 만들어줘야함
    for col in range(n):
        for st in range(0, n - m + 1):
            temp_str = ""
            for k in range(st, st+m):
                temp_str += arr[k][col]
            result = isCheck(temp_str)
            if result:
                return temp_str

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [input() for _ in range(n)]

    result = cc()
    print('#{tc} {result}')