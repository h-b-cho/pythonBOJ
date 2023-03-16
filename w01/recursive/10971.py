import sys
input = sys.stdin.readline

def circuit(start, now, depth):
    if depth == N:
        if len(temp)==4:
            sum_of_cost.append(sum(temp))
    else:
        for i in range(N):
            temp.append(W[now][i])
            circuit(start, i, depth + 1)
            temp.pop()
            
N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]
temp = []
sum_of_cost = [1e9]
for i in range(N):
    circuit(i, i, 0)
print(min(sum_of_cost))