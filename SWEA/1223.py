# 3+4+5*6+7

for tc in range(1, 11):
    n = int(input())
    s = input()
    result = ''
    st = []
    # step1. 후위 계산법으로 만들기
    for i in s:
        if i.isdecimal(): # 숫자면 result에 바로 넣기
            result += i
        else:
            if i == '+':
                if len(st) == 0: # 스택이 비어 있으면 스택에 넣기
                    st.append(i)
                else: # 스택이 비어있지 않다면
                    if st[-1] == '+' or st[-1] == '*':
                        result += st.pop()
                    st.append(i)

            elif i == '*':
                if len(st) == 0 or st[-1] == '+':
                    st.append(i)
                else:
                    if st[-1] == '*':
                        result += st.pop()

                    st.append(i)
    while st:
        result += st.pop()

    # 후위 연산법 구한거 계산하기
    st_cal = []
    for i in range(len(result)):
        if result[i].isdecimal():
            st_cal.append(result[i])
        elif result[i] == '+':
            a = int(st_cal.pop())
            b = int(st_cal.pop())
            st_cal.append(a+b)
        elif result[i] == '*':
            a = int(st_cal.pop())
            b = int(st_cal.pop())
            st_cal.append(a*b)

    print(f'#{tc} {st_cal[0]}')

