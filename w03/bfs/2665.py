import sys
import heapq
input = sys.stdin.readline
N = int(input())
graph = [[] for _ in range(N)]
for i in range(N):
    graph[i] = list(map(int, input().rstrip()))

visit = [[0] * N for _ in range(N)]
visit[0][0] = 1

heap = []
heapq.heappush(heap, [0, 0, 0])

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def dijkstra():
    global heap
    while heap:
        cnt, x, y = heapq.heappop(heap)
        if x==N-1 and y==N-1:
            print(cnt)
            return
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx< N and 0<=ny< N and visit[nx][ny]==0:
                visit[nx][ny] = 1
                if graph[nx][ny]==0:
                    heapq.heappush(heap, [cnt+1, nx, ny])
                else:
                    heapq.heappush(heap, [cnt, nx, ny])

dijkstra()