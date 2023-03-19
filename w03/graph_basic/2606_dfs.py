import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N = int(input())
M = int(input())

graph = [[0] * (N+1) for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(M):
    x, y = map(int, input().split())
    graph[x][y] = graph[y][x] = 1

cnt = 0

def dfs(n):
    global cnt
    visited[n] = 1
    for i in range(1, N+1):
        if visited[i]==0 and graph[n][i]==1:
            cnt += 1
            dfs(i)

visited[1] = 1
dfs(1)
print(cnt)