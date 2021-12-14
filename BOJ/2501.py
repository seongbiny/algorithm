n, k = map(int, input().split())
# n 의 약수를 모두 구한 다음에 k번째 숫자를 찾는다.

cnt = 0
for i in range(1, n+1):
    if n % i == 0:
        cnt += 1
        if cnt == k:
            print(i)
if cnt < k:
    print(0)