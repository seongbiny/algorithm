T = int(input())
for tc in range(1, T+1):
    arr = input()

    st = []
    result = 1
    for c in arr:
        if c == '(' or c == '{':
            st.append(c)
        elif c == ')' or c == '}':
            if st:
                pop = st.pop()
            else:
                result = 0
            if pop == '(' and c == '}':
                result = 0
            if pop == '{' and c ==')':
                result = 0

    if st:
        result = 0

    print(f'#{tc} {result}')

#확인 해볼 testcase
#(()
#({)
#()}
#()})
#({)}
