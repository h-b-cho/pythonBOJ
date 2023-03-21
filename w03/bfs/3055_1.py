from collections import deque
R, C = map(int, input().split())
graph = [list(input()) for _ in range(R)]
visited = [[False] * C for _ in range(R)]

dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)

sx, sy = 0, 0
for r in range(R):
    for c in range(C):
        if graph[r][c] == "S":
            sx, sy = r, c
            graph[r][c] = "."

def flood():
    water = []
    for r in range(R):
        for c in range(C):
            if graph[r][c] == "*" and not visited[r][c]:
                water.append((r, c))
                visited[r][c] = True
    for x, y in water:
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny]:
                if graph[nx][ny] == ".":
                    graph[nx][ny] = "*"

def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = True
    cnt = 0

    while q:
        cnt += 1
        flood()
        for _ in range(len(q)):
            x, y = q.popleft()
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny]:
                    if graph[nx][ny] == ".":
                        q.append((nx, ny))
                        visited[nx][ny] = True
                    elif graph[nx][ny] == "D":
                        return cnt
    else: 
        return "KAKTUS"

print(bfs(sx, sy))