
T = int(input())
for tc in range(1, T+1):
    str = input()
    st = []

    for i in range(len(str)):
        if len(st) == 0:
            st.append(str[i])
        elif str[i] != st[-1]:
            st.append(str[i])
        else:
            st.pop(-1)

    print(f'#{tc} {(len(st))}')




