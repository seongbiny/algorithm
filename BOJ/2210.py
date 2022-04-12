import sys
input = sys.stdin.readline

arr = [list(map(str, input().split())) for _ in range(5)]

dy = [1,0,-1,0]
dx = [0,1,0,-1]
def dfs(y, x, num):
    if len(num) == 6: # 재귀 탈출조건
        if num not in result:  # 6글자이고 result 리스트에 없으면 넣어준다.
            result.append(num)
        return
    for k in range(4): # 4방향으로 돌아준다.
        ny = y + dy[k] # 왔던 길 또 갈수 있으니까 방문체크는 안해줘도 됨
        nx = x + dx[k]
        if 0<=ny<5 and 0<=nx<5:
            dfs(ny, nx, num+arr[ny][nx])

result = []
for j in range(5): # (0,0) ~ (4,4) 모두 돌면서 시작점으로 잡아준다
    for i in range(5):
        dfs(j,i, arr[j][i])
print(len(result))

'''
5x5 행렬 갔던곳 또 갈수있으니까 방문체크 따로 안해줘도 됨
대신 종료조건인 6자리의 수 일때와 중복되지 않게 같은 숫자들이면 갯수 체크 안해주는거 2개만 신경써주면 됨
'''