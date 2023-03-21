import sys
import heapq
input = sys.stdin.readline
N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append((y, 1))

distance = [1e9] * (N+1)

q = []

def dijkstra(start):
    global q
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for j in graph[now]:
            cost = dist + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
                heapq.heappush(q, (cost, j[0]))

dijkstra(X)

answer = []
for i in range(1, N+1):
    if distance[i] == K: answer.append(i)

if len(answer) == 0: 
    print(-1)
else:
    for i in answer: 
        print(i, end='\n')