def isCheck(str):
    #str이 회문이면 true
    #아니면 false를 return

def cc():
    회문을 찾아서 return 하는 함수
    # 가로축
    for row in range(n):
        for st in range(0, n - m + 1):
            result = isCheck(arr[row][st:st + m])
            if result:
                return arr[row][st:st+m]

    # 세로축
    # 세로축은 슬라이싱 안돼 반복문으로 문자열 만들어줘야함

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [input() for _ in range(n)]

    result = cc()
    print('#{tc} {result}')