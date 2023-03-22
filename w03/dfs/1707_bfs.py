import sys
from collections import deque
input = sys.stdin.readline
K = int(input())

for _ in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    board = [int(0) for _ in range(V+1)]
    cnt = 0
    result = "YES"

    def bfs(start, color):
        global cnt, result
        queue = deque([(start, color)])
        while queue:
            curr, curr_color = queue.popleft()
            board[curr] = curr_color
            for curr_adjacent in graph[curr]:
                if board[curr_adjacent]==0:
                    queue.append((curr_adjacent, -curr_color))
                elif board[curr_adjacent]==curr_color:
                    result = "NO"
                    return

    for i in range(1, V+1):
        if board[i]==0:
            bfs(i, 1)

    print(result)