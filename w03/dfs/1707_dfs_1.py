import sys
sys.setrecursionlimit(10**6)
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

    def dfs(curr, color):
        global cnt, result
        board[curr] = color
        for curr_adjacent in graph[curr]:
            if board[curr_adjacent]==0:
                dfs(curr_adjacent, -color)
            elif board[curr_adjacent]==color:
                result = "NO"
                return

    # dfs(1, 1) <---wrong!! 이 문제에서는 그래프가 불연결 그래프일 수도 있기 때문에 모든 정점에서 출발하여 DFS 탐색을 수행해야.
    for i in range(1, V+1):
        if board[i]==0:
            dfs(i, 1)

    print(result)