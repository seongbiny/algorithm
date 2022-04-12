'''
입력방식이 정점과 간선을 주는것같아서 일단 그래프로 받음
아니 문제가 이해가 안가 ...........................
'''

import sys
input = sys.stdin.readline

n, m = map(int,input().split())
graph = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

print(graph)

