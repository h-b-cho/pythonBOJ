import sys
from sys import maxsize
import heapq
input = sys.stdin.readline
N = int(input())
M = int(input())

graph = [ list() for _ in range(N+1) ]

for _ in range(1, M+1):
    s, e, cost = map(int, input().split())
    graph[s].append([e, cost])

S, E = map(int, input().split())

visited = [maxsize]*(N+1)
tmpcost = 0
q = []

def dijkstra(n):
    global tmpcost, q
    heapq.heappush(q, (0, n)) # (비용, 시작도시). 처음 시작할 땐 비용 0.
    visited[n] = 0 
    while q:
        cost, current = heapq.heappop(q)
        if visited[current] < cost:
            continue
        for curr in graph[current]:
            tmpcost = cost+curr[1]
            if tmpcost < visited[curr[0]]:
                visited[curr[0]] = tmpcost
                heapq.heappush(q, (tmpcost, curr[0]))

dijkstra(S)
print(visited[E])
