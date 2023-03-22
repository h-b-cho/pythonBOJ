import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]      # 간선 정보를 담고 있음.
infoarr = [[0]*(N+1) for _ in range(N+1)] # 특정부품을 만드는 데에 필요한 부품 번호, 갯수 정보.
inDegree = [0 for _ in range(N+1)]    # 진입차수 배열. (진입차수가 0이 되었다면, 큐에 해당 정점을 삽입)
q = deque() # wrong!!!!! q = deque([])

for _ in range(M):
    X, Y, K = map(int, input().rstrip().split())
    graph[Y].append([X, K]) # wrong!!!!! graph[X].append([Y, K])
    inDegree[X] += 1        # wrong!!!! inDegree[Y] += K

for n in range(1, N+1):
    if inDegree[n]==0:
        q.append(n)
        infoarr[n][n] = 1

while q:
    curr_node = q.popleft()
    for next_node, cnt in graph[curr_node]:
        for i in range(1, N+1):
            infoarr[next_node][i] += cnt*infoarr[curr_node][i]
        inDegree[next_node] -= 1
        if inDegree[next_node]==0:
            q.append(next_node)

for j in range(1, N+1):
    if infoarr[N][j]:
        print(f'{j} {infoarr[N][j]}')