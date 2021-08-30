T = int(input())
for tc in range(1, T+1):
    word = input()
    lst = ''
    for i in range(1, 11):
        if word[0:i] == word[i:i+i]:
            lst += word[0:i]
            break

    print(f'#{tc} {len(lst)}')


