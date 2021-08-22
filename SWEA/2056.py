T = int(input())
for tc in range(1, T+1):
    date = list(map(int, input()))
    print(date)

    # print(f'#{tc}', end=' ')
    # if date[0] != 0:
    #     print(f'{date[0]}{date[1]}{date[2]}{date[3]}',end="/")
    #     if date[4] < 2:
    #         if 0 < date[5] < 10:
    #             print(f'{date[4]}{date[5]}', end="/")
    #             if date[6] < 4:
    #                 if date[7] < 10:
    #                     print(f'{date[6]}{date[7]}')
    #                 else: print(-1)
    #             else: print(-1)
    #         else: print(-1)
    #     else: print(-1)
    # else: print(-1)

    for y in range(0,4):
        if date[0] != 0:
            print(f'{date[y]}', end='')
        else:
            print(-1)
            pass
    for m in range(4,6):
        if date[4] < 3:
            if date[5] < 10:
                print(f'{date[m]}', end='')
        else:
            print(-1)
            pass

    for d in range(6,8):
        if date[6] < 4:
            if date[7] < 10:
                print(f'{date[d]}', end='')
        else:
            print(-1)
            pass


        # 슬라이싱 !

