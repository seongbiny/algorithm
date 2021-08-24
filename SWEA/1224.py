def step1(s): # 중위표기법을 후위표기법으로
    t = [] # 후위 표기법
    st = [] # 연산자
    for c in s:
        if c.isdecimal():
            t.append(c)
        elif c == ')': # '(' 만날때까지 스택으로 보내고 '('는 버림
            while t[-1] != '(':
                t.append(st.pop())
            t.pop()
        else:
            #스택 안 연산자의 우선순위가 낮거나 같으면 pop 해서 t 로 보냄
            while st and not out_st[c] > in_st[st[-1]]:
                t.append(st.pop())
            st.append(c)
    while st:
        t.append(st.pop())
    return t


def step2(t):
    st = []
    for c in t:
        if c.isdecimal():
            st.append(c)
        else:
            n1 = int(st.pop())
            n2 = int(st.pop())
            if c == '+':
                st.append(n2+n1)
            if c == '*':
                st.append(n2*n1)
    return st.pop()
T = 10

in_st = {'+':1, '*':2, '(':0}
out_st = {'+':1, '*':2, '(':3}

for tc in range(1, 11):
    length = int(input())
    word = input()

    result = step2(step1(word))
    print(f'#{tc} {result}')