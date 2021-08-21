# 여는 괄호가 몇개 닫는 괄호가 몇개이지 세는 문제
# ( 쌓일때 cnt+=1 , 레이저 맞으면 sum += cnt ) 나오면 cnt -1, sum +1

T = int(input())
for tc in range(1, T+1):
    arr = input()

    cnt = 0
    sum = 0

    for i in range(len(arr)):
        if arr[i] == '(':
            cnt += 1
        elif arr[i] == ')':
            if arr[i-1] == '(':
                cnt -= 1
                sum += cnt
                continue
            if arr[i-1] == ')':
                cnt -= 1
                sum += 1

    print(f'#{tc} {sum}')
