import sys
input = sys.stdin.readline
N = int(input())
W = list(list(map(int, input().split())) for _ in range(N))
    
arr = [0]*N
p = []
permuts = []

def permu(n):
    global p
    if n==N:
        permuts.append(p)
        return
    for i in range(N):
        if arr[i]==0:
            arr[i] = 1
            p.append(i)
            permu(n+1)
            arr[i] = 0
            p = p[:-1]
permu(0)
# print(permuts)

currMin = 1e9

for perm in permuts:
    sum = 0
    flag = True
    if W[perm[-1]][perm[0]]==0:
        continue
    for i in range(N-1):
        if W[perm[i]][perm[i+1]]==0:
            flag = False
            break
        sum += W[perm[i]][perm[i+1]]
    # if not flag:
    #     continue 
    if flag:
        sum += W[perm[-1]][perm[0]]
        currMin = min(sum, currMin)
print(currMin)