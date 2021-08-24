T = int(input()) # 테스트케이스 개수 받기
for tc in range(1, T+1): # 테스트케이스 만큼 돌리기
    arr = input() # 검사할 문자열 받기

    st = [] # 검사할 괄호를 넣어주는 빈 스택
    result = 1
    for c in arr: # 문자열을 하나씩 돌려주면서 검사한다
        if c == '(' or c == '{':
            st.append(c)
        elif c == ')' or c == '}':
            if st: # 스택에 뭐가 들어있다면/ 비어있지않다면
                pop = st.pop() # 마지막에 들어있는걸 꺼낸다
                if pop == '(' and c == '}': # 꺼낸 괄호와 짝이 안맞으면
                    result = 0
                if pop == '{' and c == ')': # 꺼낸 괄호와 짝이 안맞으면
                    result = 0
            else: # 스택이 비어있다면
                result = 0
                # 앞에 괄호가 없었는데 닫힌괄호부처 나온것이니 에러


    if st:
        result = 0

    print(f'#{tc} {result}')

#확인 해볼 testcase
#(()
#({)
#()}
#()})
#({)}
