T = int(input())
for tc in range(1, T+1):
    N = int(input())
    happy = []
    for i in range(N):
        happy.append(int(input()))
    happy.pop(0)
