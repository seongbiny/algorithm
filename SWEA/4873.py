
T = int(input())
for tc in range(1, T+1):
    str = input()
    st = []
    st.append(str[0])
    for i in range(1,len(str)):

        if str[i] != st[-1]:
            st.append(str[i])
        else:
            st.pop(-1)

    print(f'#{tc} {(len(st))}')











