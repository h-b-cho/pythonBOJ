# 정답 참고하여 풀이

import sys
from collections import deque
input = sys.stdin.readline
N, K = map(int, input().split())
visited = [0 for _ in range(100001)]

def bfs(n, k):
    q = deque([n])
    visited[n] = 1
    while q:
        curr = q.popleft()
        if curr == k:
            return visited[curr] - 1
        for moved in ((curr-1), (curr+1), (2*curr)):
            if 0 <= moved <= 100000 and not visited[moved]: 
                visited[moved] = visited[curr] + 1
                q.append(moved)

result = bfs(N, K)
print(result)