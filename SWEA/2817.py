
def powerset(k, sumV):
    global cnt
    if sumV == K:
        cnt += 1
        return
    if sumV > K or k >= N:
        return

    powerset(k+1, sumV)
    powerset(k+1, sumV+A[k])

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    A = list(map(int,input().split()))
    cnt = 0
    res = [-1] * N
    powerset(0,0)

    print(cnt)