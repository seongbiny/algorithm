T = int(input())
for tc in range(1, T+1):
    word = list(input())
    st = []

    for i in word:
        if i not in st:
            st.append(i)
        else:
            st.remove(i)
    st = sorted(st)
    if len(st) == 0:
        print(f'#{tc} Good')
    else:
        print(f'#{tc} {"".join(st)}')

'''
    i = 0
    while i < len(word): # 0 1
        st.append(word[i])
        if i == len(word)-1:
            #st.append(word[i])
            break
        elif st[-1] == word[i+1]:
            st.pop(-1)
            i += 2
        elif st[-1] == word[i]:
            st.pop(-1)
            i += 1
        else:
            i += 1

    if len(st) == 0:
        print(f'#{tc} Good')
    else:
        print(f'#{tc} {sorted(st)}')
'''


