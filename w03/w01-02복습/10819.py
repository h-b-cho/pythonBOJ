import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
currMax = -1e999
visited = [0]*N
arr = []
sum = 0

def dfs(depth):
    global sum, currMax
    if depth==N:
        for i in range(N-1):
            sum += abs(arr[i]-arr[i+1])
        if sum>currMax:
            currMax = sum
        sum = 0
        return
    for i in range(N):
        if visited[i]==0:
            arr.append(A[i])
            visited[i] = 1
            dfs(depth+1)
            arr.pop()
            visited[i] = 0
dfs(0)
print(currMax)