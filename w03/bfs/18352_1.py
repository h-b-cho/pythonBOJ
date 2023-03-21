import sys
from collections import deque
input = sys.stdin.readline
N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)

distance = [0] * (N+1)
visited = [0] * (N+1)

q = deque()

def bfs(start):
    answer = []
    q = deque([start])
    visited[start] = 1
    distance[start] = 0
    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                visited[i] = 1
                q.append(i)
                distance[i] = distance[now] + 1
                if distance[i]==K:
                    answer.append(i)
    if len(answer)==0:
        print(-1)
    else:
        answer.sort()
        for i in answer:
            print(i, end='\n')

bfs(X)