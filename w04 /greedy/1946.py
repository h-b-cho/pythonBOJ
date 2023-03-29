import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N = int(input())
    rank = [[] for _ in range(N) ]
    for i in range(N):
        test, itvw = map(int, input().split())
        rank[i].append(test)
        rank[i].append(itvw)
    rank.sort(key=lambda x:(x[0]))

    temp = rank[0][1]
    cnt = 1

    for j in range(len(rank)):
        if temp > rank[j][1]:
            cnt += 1
            print(rank[j])
            temp = rank[j][1]
