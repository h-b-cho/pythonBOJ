import sys
input = sys.stdin.readline

def BFS(si, sj, ei, ej): #start, end
    q = []
    visited = [ [0]*M for _ in range(N) ]

    q.append((si, sj))
    visited[si][sj] = 1

    while q:
        ci, cj = q.pop(0) #curr

        if (ci, cj)==(ei, ej):
            return( visited[ei][ej] )

        #4방향, 범위 내, 조건에 맞으면 가야 할 길~
        for di, dj in ((-1,0), (1,0), (0,-1), (0,1)):
            ni, nj = ci+di, cj+dj #next
            if 0<=ni<N and 0<=nj<M and graph[ni][nj]==1 and visited[ni][nj]==0:
                q.append((ni, nj))
                visited[ni][nj] = visited[ci][cj]+1

N, M = map(int, input().split())
graph = [ list(map(int, input().strip())) for _ in range(N) ]

result = BFS(0, 0, N-1, M-1)
print(result)