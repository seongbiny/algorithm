T = int(input())
for tc in range(1, T+1):
    word = input()
    alpha = ['a', 'e', 'i', 'o', 'u']
    result = ''
    for i in word:
        if i not in alpha:
            result += i

    print(f'#{tc} {result}')