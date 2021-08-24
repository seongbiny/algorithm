def step1(s):  # 중위표기법을 후위표기법으로 바꾸는 작업
    isp = {'*': 2, '+': 1} #'(' ')'
    t = []
    st = []
    for c in s:
        if c.isdecimal():
            t.append(c)
        else:
            if len(st) == 0 or isp[st[-1]] < isp[c]:
                st.append(c)
            else:
                while st and isp[st[-1]] >= isp[c]:
                    t.append(st.pop())
                st.append(c)
    while st:
        t.append(st.pop(-1))
    return t

def step2(t): # 숫자면 스택에 넣고 연산자면 st에서 숫자를 pop해서 연산 후 결과를 st에 넣는다.
    st = []
    for c in t:
        if c.isdecimal():
            st.append(c)
        else:
            n1 = int(st.pop())
            n2 = int(st.pop())
            if c == '+':
                st.append(n1+n2)
            if c == '*':
                st.append(n1*n2)
    return st.pop()

T = 10
for tc in range(1, T+1):
    n = int(input())
    s = input()
    result = step2(step1(s))
    print(f'#{tc} {result}')




