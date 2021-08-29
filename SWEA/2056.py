T = int(input())
for tc in range(1, T+1):
    date = input()

    year = date[:4]
    mon = date[4:6]
    day = date[6:8]
    day_dict = {1: 31, 2: 28, 3: 31, 4: 40, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    if (int(mon) >= 13) or (int(mon) <= 0):
        print(f'#{tc} -1')
        continue
    else:
        if day_dict[int(mon)] < int(day) or int(day) <= 0:
            print(f'#{tc} -1')
            continue
        else:
            print(f'#{tc} {year}/{mon}/{day}')








