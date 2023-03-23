# 시험 시간에 못 풀었음!!

import sys
from collections import deque
input = sys.stdin.readline
n, k = map(int, input().split())
pipe = [list(map(int, input().split())) for _ in range(n)]
S, X, Y = map(int, input().split())

virus = [[] for _ in range(k+1)]

for i in range(n):
    for j in range(n):
        if pipe[i][j] != 0:
            v = pipe[i][j]

visited = [[0]* n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = []
for x in range(n):
    for y in range(n):
        if not visited[x][y] and pipe[x][y] !=0:
            val = pipe[x][y]
            q.append((val, x, y))
            visited[x][y] = 1

cnt = 0
while True:
    if cnt == S:
        break
    q = deque(sorted(list(q)))
    for _ in range(len(q)):
        value, a, b = q.popleft()            
        for m in range(4):
            nx = a + dx[m]
            ny = b + dy[m]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and pipe[nx][ny] == 0:
                pipe[nx][ny] = value
                visited[nx][ny] = 1
                q.append((value, nx, ny))
    cnt += 1

ans = pipe[X-1][Y-1]
print(ans)