import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N, M = map(int, input().split()) 

graph = [[0] * (N+1) for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u][v] = graph[v][u] = 1

def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = 1 
    while q:
        v = q.popleft()
        for i in range(1, N+1):
            if visited[i]==0 and graph[v][i]==1:
                q.append(i)
                visited[i] = 1

cnt = 0

for i in range(1, N+1):
    if not visited[i]:
        if not graph[i]:
            cnt += 1
            visited[i] = 1
        else:
            bfs(i)
            cnt += 1

print(cnt)