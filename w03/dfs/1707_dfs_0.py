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

    def dfs(curr):
        global cnt
        for curr_adjacent in graph[curr]:
            if board[curr_adjacent]==int(0):
                cnt+=1
                if cnt%2==1:
                    board[curr_adjacent] = -1
                else:
                    board[curr_adjacent] = 1
                dfs(curr_adjacent)
    dfs(1)

    result = "YES"

    for i in range(1, len(board)-1):
        if board[i]==board[i+1]:
            result = "NO"

    print(result)
