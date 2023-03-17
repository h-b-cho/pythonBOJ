import sys
input = sys.stdin.readline
N = int(input())
W = list(list(map(int, input().split())) for _ in range(N))
currMin = 1e9
visited = [0]*N

def dfs(depth, current, sum):
    global currMin
    if depth==N-1 and W[current][0]!=0:
        sum+=W[current][0]
        if sum<currMin:
            currMin = sum
        return
    for i in range(N):
        if visited[i]==0 and W[current][i]!=0:
            visited[i] = 1
            dfs(depth+1, i, sum+W[current][i])
            visited[i] = 0

visited[0] = 1
dfs(0, 0, 0)
print(currMin)