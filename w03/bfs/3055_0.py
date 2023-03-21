import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().split())
graph = [ list(map(str, input().rstrip())) for _ in range(R) ]

visited = [[0 for _ in range(C)] for _ in range(R)]
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)

queue = deque([])
water = deque([])

for r in range(R):
    for c in range(C):
        if graph[r][c] == "S": queue.append([r, c]) # 고슴도치의 시작하는 지점 설정.
        if graph[r][c] == "*": water.append([r, c]) # 물의 시작하는 지점 설정.

def flood():
    global water
    for r in range(R):
        for c in range(C):
            if graph[r][c] == "*" and not visited[r][c]:
                water.append([r, c])
                visited[r][c] = 1
    for cx, cy in water:
        for dx, dy in ((-1,0), (1,0), (0,-1), (0,1)):
            nx, ny = cx+dx, cy+dy
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny]:
                if graph[nx][ny] == ".":
                    graph[nx][ny] = "*"

def bfs():
    global queue
    while queue:
        try: 
            flood()
            for _ in range(len(queue)):
                cx, cy = queue.popleft()
                for dx, dy in ((-1,0), (1,0), (0,-1), (0,1)):
                    nx, ny = cx+dx, cy+dy
                    if 0<=nx<R and 0<=ny<C and graph[nx][ny]=="." and not visited[nx][ny]:
                        if graph[nx][ny]=="D":
                            print (  visited[nx][ny] + 1 )
                        else:
                            visited[nx][ny] = visited[cx][cy] + 1
                            queue.append([nx, ny])
        except:
            print ( "KAKTUS" )

bfs()