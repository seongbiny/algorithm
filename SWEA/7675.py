upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q'
    , 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
         'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z']
a = ['.', '!', '?']
T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 문장의 개수
    sentence = list(map(str, input().split()))
    result = ['0'] * N  # 이름인 경우를 세서 넣어주는 리스트
    # print(sentence)
    cnt = 0  # 이름일 조건이 맞는 단어를 세는 변수
    check = 0  # 문장의 개수를 세는 변수
    for i in range(len(sentence)):
        if sentence[i][0].isupper():  # 단어의 첫 시작이 대문자 일 경우
            # print(sentence[i])
            if len(sentence[i]) == 1 or sentence[i][-1].islower() or sentence[i][-1] in a:
                cnt += 1  # 이름 조건에 충족하면 + 1
                if sentence[i][-1] in a:
                    if sentence[i][-2] not in lower:
                        cnt = 0
                        check += 1
                    else:
                        check += 1
                        result[check - 1] = str(cnt)
                        cnt = 0

    print(f'#{tc} {" ".join(result)}')

'''
테스트케이스 2개 돌리면 출력 제대로 나오는데
#1 3 0
#2 2 0 1
왜 제출하면 11개 중 0개 맞았다고 뜨나여 ?
'''