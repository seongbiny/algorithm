T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split()) # n: 뿔 수 m: 동물 수
    # 2개씩 뺀 다음 남은 뿔수랑 남은 동물수랑 같으면 그게 유니콘수

    twin = 0
    uni = 0
    for i in range(m): #0 1 2
        if n != (m-i):
            n -= 2
            twin += 1
        elif n == m-i:
            n -= 1
            uni += 1
    print(f'#{tc} {uni} {twin}')



