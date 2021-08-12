T =10
for tc in range(1, T+1):
    n = int(input())
    h = list(map(int, input()))

    dx = [-2, -1, 1, 2]
    cnt = 0
    lst = []
    for i in range(2,len(h)):
        for j in range(4):
            if j==1 or j==2:
                if h[i+dx[j]] > h[i]:
                    pass
            else:
                h[j] - h[i+dx[j]]


