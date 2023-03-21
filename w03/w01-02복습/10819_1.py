# 01
import sys
from itertools import permutations
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
perms = []
for p in permutations(A, N):
    perms.append(p)

currMax = -1e99
tmp = 0

for p in perms:
    tmp = 0
    for i in range(N-1):
        tmp += abs(p[i] - p[i+1])
    if tmp > currMax:
        currMax = tmp

print(currMax)

# 02
import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
currMax = -1e99
tmp = 0
arr = []
visited = [0]*N

def dfs(depth):
    global currMax, tmp
    if depth==N:
        for i in range(N-1):
            tmp += abs(arr[i] - arr[i+1])
        if tmp > currMax:
            currMax = tmp
        tmp = 0
        return
    for i in range(N):
        if visited[i]==1:
            continue
        arr.append(A[i])
        visited[i] = 1
        dfs(depth+1)
        arr.pop()
        visited[i] = 0

dfs(0)
print(currMax)