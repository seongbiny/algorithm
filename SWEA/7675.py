end_point = ['.', '!', '?']
T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 문장의 개수
    sentence = list(map(str, input().split()))
    name_cnt = 0
    result = []
    for i in sentence:
        # 대문자 1개
        # 대문자로 시작 소문자로 끝끝
        if len(i) == 1:
            if i[0].isupper():
                name_cnt += 1
        else:
            if i[-1] in end_point:
                if i[0].isupper() and i[1:len(i)-1].islower() and i[1:len(i)-1].isalpha():
                    name_cnt += 1
                result.append(str(name_cnt))
                name_cnt = 0
            else:
                if i[0].isupper() and i[1:].islower() and i[1:].isalpha():
                    name_cnt += 1

    print(f'#{tc} {" ".join(result)}')

