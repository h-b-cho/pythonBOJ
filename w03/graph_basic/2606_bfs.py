import sys
from collections import deque
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
q = deque()

def bfs(n):
    global cnt
    q.append(n)
    visited[n] = 1
    while q:
        n = q.popleft()
        for i in range(1, N+1):
            if graph[n][i]==1 and visited[i]==0:
                cnt+=1
                q.append(i)
                visited[i] = 1

for j in range(1, N+1):
    if graph[j]==[1] and visited[j]==[0]:
        bfs(j)

bfs(1)
print(cnt)