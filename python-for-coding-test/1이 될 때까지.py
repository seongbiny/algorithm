n, k = map(int, input().split())

cnt = 0
while True:
    if n == 1:
        break
    elif n % k != 0:
        n -= 1
        cnt += 1
    else:
        n //= k
        cnt += 1

print(cnt)

'''
1이 되기까지 최소로 수행해야하므로 n이 k로 나누어지면 나누고, 안나누어지면 1씩 빼준다.
'''