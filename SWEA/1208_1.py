T = 10
for tc in range(1, 11):
    dump = int(input()) # 덤프 횟수
    box = list(map(int,input().split())) # 상자 높이를 담는 리스트

    # 박스를 최솟값을 가진 개수 -1, 최솟값+1 개를 가진 박스 수 +1
    # 박스를 최댓값을 가진 개수 -1, 최댓값+1 개를 가진 박스 수 +1
    # 최솟값 == 최댓값
    result = 0
    cnt = 0
    while cnt < dump:
        min_box = box[0]
        max_box = box[0]
        max_index = 0
        min_index = 0
        for i in range(len(box)):
            if max_box >= box[i]:
                max_box = box[i]
                max_index = i
            if min_box <= box[i]:
                min_box = box[i]
                min_index = i
        max_box -= 1
        min_box += 1
        max_index -= 1
        min_index += 1
        cnt += 1

        if min_box == max_box:
            result = 0
            break
        box[min_box] = min_box
        box[max_box] = max_box
        result = max_box - min_box
    print(f'#{tc} {result}')




