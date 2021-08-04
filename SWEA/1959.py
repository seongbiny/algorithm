T = int(input())

for i in range(1, T+1):
    n, m =map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    c = []

    if n==m:
        result = 0
        for i in range(n):
            result += a[i]*b[i]
        print(result)

    elif m > n:   #00+11 / 01+12
        for k in range(m - n + 1): #0 1
            result = 0
            for j in range(n): #0 1
                result += int((a[j]*b[k+j]))
            c.append(result)
        print(f'#{i} {max(c)}')


    else:
        for k in range(n - m + 1): # 0 1
            result = 0
            for j in range(m): # 0 1
                result += int((a[j+k]*b[j])) #00+11 / 10+21
            c.append(result)
        print(f'#{i} {max(c)}')
