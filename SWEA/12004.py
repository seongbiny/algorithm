T = int(input())
for tc in range(1, T+1):
    target = int(input())
    check = 0
    for i in range(1, 10): # 1 2 3 4 5 6 7 8 9
        for j in range(1, 10): # 1 2 3 4 5 6
            if i * j == target:
                check += 1


    if check == 0:
        print(f'#{tc} No')
    elif check > 0:
        print(f'#{tc} Yes')




