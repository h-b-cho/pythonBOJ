import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [int(0) for _ in range(N+1)]

def dfs(curr):
    for curr_adjacent in graph[curr]:
        if parent[curr_adjacent]==int(0):
            parent[curr_adjacent] = curr
            dfs(curr_adjacent)

dfs(1)
# for x in range(2, N+1): print(parent[x])
print(parent)