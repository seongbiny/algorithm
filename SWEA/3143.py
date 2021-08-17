#import sys
#sys.stdin = open("input_3143.txt","r")

T = int(input())
for tc in range(1, T+1):
    a, b = input().split()
    n = len(a)
    m = len(b)
    cnt = 0
    result = 0

    for i in range(n-m+1):
        if a[i:i+m] == b:
            cnt += 1

    result = cnt + n - (cnt*m)
    print(f'#{tc} {result}')

