import sys
sys.stdin = open("input_1219.txt","r")

def dfs(v):
    global ans
    if v == 99:
        ans = 1
        return

    visited[v] = True

    for w in range(100):
        if not visited[w] and arr[v][w]:
            dfs(w)

for _ in range(1, 11):
    V = 99
    tc, E = map(int, input().split())
    road = list(map(int, input().split()))
    arr = [[0] * (V+1) for _ in range(V+1)]

    for i in range(E):
        arr[road[2*i]][road[2*i+1]] = 1

    visited = [0] * 100
    ans = 0

    dfs(0)
    print(f'#{tc} {ans}')

