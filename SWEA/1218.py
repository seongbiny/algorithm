for tc in range(1,11):
    n = int(input())
    lst = list(map(str, input()))

    st = []
    for i in range(n):

        if lst[i] == ')' and st[-1] == '(':
            st.pop()
        elif lst[i] == ']' and st[-1] == '[':
            st.pop()
        elif lst[i] == '}' and st[-1] == '{':
            st.pop()
        elif lst[i] == '>' and st[-1] == '<':
            st.pop()
        else:
            st.append(lst[i])

    if not st:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
