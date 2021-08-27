T = int(input())
for tc in range(1, T+1):
    n = int(input())
    lst = list(map(int, input().split()))

    result = -1
    multiply = []

    for i in range(n):
        for j in range(i+1, n):
            multiply.append(lst[i] * lst[j])
    multiply2 = list(map(str, multiply)) # ['8', '14', '20', '28', '40', '70']

    for i in multiply2:
        if len(i) < 2:
            multiply.remove(int(i))
        elif len(i) > 1:
            a = ''.join(sorted(i))
            if i != a:
                multiply.remove(int(i))
        result = max(multiply)

    print(f'#{tc} {result}')









