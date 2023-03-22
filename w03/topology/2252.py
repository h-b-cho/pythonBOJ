import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
inDegree = [0 for _ in range(N+1)] # 진입차수 배열 (진입차수가 0이 되었다면, 큐에 해당 정점을 삽입)
queue = deque()

for _ in range(M):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    inDegree[b] += 1

for i in range(1, N+1):
    if inDegree[i]==0:
        queue.append(i)

while queue:
    student = queue.popleft()
    print(student, end=' ')
    for v in graph[student]:
        inDegree[v] -= 1
        if inDegree[v]==0:
            queue.append(v)