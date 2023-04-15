import sys
from itertools import permutations
input = sys.stdin.readline

N = int(input())
W = list(list(map(int, input().split())) for _ in range(N))

currMin = 1e9
costlist = list(permutations(range(N)))

for cost in costlist:
    sum = 0
    flag = True
    if W[cost[-1]][cost[0]] == 0:
        continue
    for i in range(N-1):
        if W[cost[i]][cost[i+1]] == 0:
            flag = False
            break
        sum += W[cost[i]][cost[i+1]]
    if flag:
        sum += W[cost[-1]][cost[0]]
        currMin = min(currMin, sum)
print(currMin)