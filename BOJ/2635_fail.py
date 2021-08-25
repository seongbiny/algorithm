num = int(input())

max_result = []
for i in range(1, num+1):
    result = []
    result.append(num)
    result.append(i)  # result = [num, i]
    idx = i
    n = 0
    while True:
        next_level = result[n] - result[n+1]
        if next_level < 0:
            break
        result.append(next_level)
        n += 1
        # else:
        #     n += 1
        max = 0
    if len(result) > max:
        print(result)
    #print(result)
    max_result.append(len(result))
    # max_result 함수의 최대값이 8 이다 8의 인덱스 번호가 result의 두번재 원소일때 리스트를 뽑아
    # 최대일때 리스트는 어떻게 뽑아야 하나여 . . .?
print(max(max_result))










