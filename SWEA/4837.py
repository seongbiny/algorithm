T =int(input())
for tc in range(1, T+1):
    n, k = map(int,input().split())
    # n = 부분집한 원소의 수, k 부분 집합의 합
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    z = len(A)
    #subset = []
    for i in range(1<<z):
        for j in range(z+1):
            if i & (1<<j):
                subset = [list(map(int, A[j])) for _ in range()]