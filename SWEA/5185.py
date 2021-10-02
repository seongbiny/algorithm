T = int(input())
for tc in range(1, T+1):
    n, jinsu = input().split()

    dict = {
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15,
    }
    result = ''
    for i in range(len(jinsu)):
        if jinsu[i] not in dict:
            a = int(jinsu[i])
        else:
            a = dict[jinsu[i]]

        num = 8
        for j in range(4):
            if a & num:
                result += '1'
            else:
                result += '0'
            num = num >> 1

    print(f'#{tc} {result}')