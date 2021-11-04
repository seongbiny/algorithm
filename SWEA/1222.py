for tc in range(1, 11):
    n = int(input())
    sik = list(input())

    st = []
    result = ''

    for s in sik:
        if s.isdecimal():
            result += s
        elif s == '+':
            while st:
                result += st.pop()
            st.append(s)
    while st:
        result += st.pop()
    #print(result)

    for i in result:
        if i.isdecimal():
            st.append(int(i))
        else:
            if i == '+':
                num1 = st.pop()
                num2 = st.pop()
                st.append(num1 + num2)

    print(f'#{tc} {st[0]}')

    # 34+5+6+7+