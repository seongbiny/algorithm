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

def cc(m):
    for i in range(n):
        for st in range(n-m+1):
            #가로
            result = isCheck(arr[i][st:st+m])
            if result:
                return True

            #세로
            temp_str = ""
            for k in range(st, st+n):
                temp_str += arr[k][i]
            result = isCheck(temp_str)
            if result:
                return False

T = int(input())
for tc in range(1, T+1):
    n = 100
    no = input()
    arr = [input() for _ in range(n)]

    for m in range(n, 2, -1):
        result = cc(m) # 길이가 m인 회문을 찾는다

        if 찾았으면:
            break

    result = cc()
    print('#{tc} {result}')