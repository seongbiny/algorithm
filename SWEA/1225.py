T = 10
for tc in range(1, 11):
    tast_case = input()
    word = list(map(int, input().split()))  # [10, 6, 12, 8, 9, 4, 1, 3]
    result = ''

    while word[-1] != '0':
        for i in range(1, 6): # 1 2 3 4 5
            a = word.pop(0)
            if a - i <= 0:
                a = 0
                word.append(a)
                word = list(map(str, word))
                result = " ".join(word)
                print(f'#{tc} {result}')
                break
            else:
                a -= i
                word.append(a)








