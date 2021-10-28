import sys
input = sys.stdin.readline

N, K = map(int, input().split())
temp = list(map(int, input().split()))

sumV = 0
start = 0
# maxV = 0
lst = []
for end in range(N): # 0 1 2 3 4 5
    sumV += temp[end]
    if end-start+1 == K:
        lst.append(sumV)
        sumV -= temp[start]
        start += 1

print(max(lst))

'''
이중포문으로 풀었다가 시간초과
maxV = 0 두고 if 크기비교 시간초과
빈 리스트생성 max() 시간초과
'''