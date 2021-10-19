T = int(input())
for tc in range(1, T + 1):
    word = str(input())
    cnt = 0

    for i in range(len(word) // 2):
        if word[i] == word[-i - 1] or word[i] == '?' or word[-i - 1] == '?':
            cnt += 1

    if cnt == len(word)//2:
        result = 'Exist'
    else:
        result = 'Not exist'

    print(f'#{tc} {result}')


'''
양 끝에서부터 검사하면서 문자가 같거나 ? 나오면 넘어간다
문자가 다르거나 양 끝 중 하나라도 ?가 없으면 not exist
'''