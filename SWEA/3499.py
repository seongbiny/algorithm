T = int(input())
for tc in range(1, T+1):
    n = int(input())
    word = list(map(str, input().split()))

    left = []
    right = []

    if n % 2 == 0:
        for i in range(n//2):
            left.append(word[i])
        for j in range(n//2, n):
            right.append(word[j])
    else:
        a = n // 2 + 1
        for i in range(a):
            left.append(word[i])
        for j in range(n // 2+1, n):
            right.append(word[j])
    #print(left)
    #print(right)

    result = []
    if len(word) % 2 == 0:
        a = len(word)//2
        for i in range(a):  # 0 1 2
            result.append(left[i])
            result.append(right[i])
    else:
        result.append(left[0])
        a = len(word)//2
        for i in range(a):  # 0 1
            result.append(right[i])
            result.append(left[i+1])

    print(f'#{tc} {" ".join(result)}')




# 리스트를 스트링으로 바꾸는 거?
# list -> str
# 조인을 쓴다! " ".join(list)