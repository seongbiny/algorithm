T = int(input())
for tc in range(1, T+1):
    A, B, C, D = map(int, input().split())

    a = A/B
    b = C/D

    if a > b:
        print(f'#{tc} ALICE')
    elif a == b:
        print(f'#{tc} DRAW')
    else:
        print(f'#{tc} BOB')


