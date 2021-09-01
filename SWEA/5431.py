T = int(input())
for tc in range(1, T+1):
    n, k = map(int, input().split()) # n: 수강생 수 k: 과제를 제출한 사람의 수
    submit = list(map(int, input().split())) # 과제 제출한 사람 번호
    result = []
    lst = []
    for i in range(1, n+1): # 1번부터 학생수만큼 번호 정렬
        lst.append(i)

    #print(f'#{tc}', end=' ')
    for i in range(n):
        if lst[i] not in submit:
            lst[i] = str(lst[i])
            result.append(lst[i])

    print(f'#{tc} {" ".join(result)}')




