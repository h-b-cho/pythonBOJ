import sys
from collections import deque
input = sys.stdin.readline
M, N, H = map(int, input().split())
box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

visited = [[[0]*M for _ in range(N)] for _ in range(H)]

dh = [0,0,1,-1,0,0]
di = [-1,1,0,0,0,0]
dj = [0,0,0,0,1,-1]

def bfs():
    # cnt = 익혀야 하는 토마토 개수.
    cnt = 0 

    q = deque()

    # q 시작할 때의 초기 설정
    for h in range(H):
        for i in range(N):
            for j in range(M):
                if box[h][i][j]==1:      # 토마토가 익었다면 q에 삽입
                    q.append((h, i, j))
                    visited[h][i][j] = 1
                elif box[h][i][j]==0:    # 토마토가 안 익었다면 cnt+1
                    cnt += 1
    while q:
        ch, ci, cj = q.popleft()
        for i in range(6):
            nh = ch+dh[i]
            ni = ci+di[i]
            nj = cj+dj[i]
            if 0<=nh<H and 0<=ni<N and 0<=nj<M and visited[nh][ni][nj]==0 and box[nh][ni][nj]==0:
                q.append((nh, ni, nj))
                visited[nh][ni][nj] = visited[ch][ci][cj]+1
                cnt -= 1
    if cnt==0:
        return visited[ch][ci][cj]-1
    else:
        return -1

print(bfs())