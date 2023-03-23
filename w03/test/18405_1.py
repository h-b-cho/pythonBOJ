import sys
import heapq
input = sys.stdin.readline
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
n, k = map(int, input().split())

world = [list(map(int, input().split())) for _ in range(n)]

s, target_y, target_x = map(int, input().split())

heap = []
for i in range(n):
    for j in range(n):
        if world[i][j] > 0:
            heapq.heappush(heap, (0, world[i][j], i, j))

while heap:
    time, virus, y, x = heapq.heappop(heap)
    if time == s:
        break
    for i in range(4):
        ny, nx = y+dy[i], x+dx[i]
        if 0 <= ny < n and 0 <= nx < n:
            if world[ny][nx] == 0:
                world[ny][nx] = virus
                heapq.heappush(heap, (time+1, virus, ny, nx))

print(world[target_y-1][target_x-1])