import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N, M = map(int, input().split()) 

graph = [[0] * (N+1) for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u][v] = graph[v][u] = 1

def dfs(v):
    visited[v] = 1
    for i in range(1, N+1):
        if visited[i]==0 and graph[v][i]==1:
            dfs(i)

cnt = 0

for i in range(1, N+1):
    if not visited[i]:
        dfs(i)
        cnt += 1

print(cnt)