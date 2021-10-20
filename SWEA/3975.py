T = int(input())
result = []
for tc in range(1, T+1):
    # A, B, C, D = map(int, input().split())
    lst = list(map(int, input().split()))

    alice = lst[0]/lst[1]
    bob = lst[2]/lst[3]

    # result = []
    if alice > bob:
        # print(f'#{tc} ALICE')
        result.append('ALICE')
    elif alice < bob:
        # print(f'#{tc} DRAW')
        result.append('BOB')
    else:
        # print(f'#{tc} BOB')
        result.append('DRAW')

for i in range(T):
    print(f'#{i+1} {result[i]}')

'''
입력 받고 바로바로 결과값을 출력하면 시간초과
결과값을 전부 다 받은 다음에 출력시켜야함 
'''