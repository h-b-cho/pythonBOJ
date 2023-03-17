def dfs():
    import sys
    from itertools import permutations
    input = sys.stdin.readline
    N = int(input())
    W = list(list(map(int, input().split())) for _ in range(N))
    cities = list(permutations(range(N)))
    currMin = 1e9

    for city in cities:
        sum = 0
        flag = True
        if W[city[-1]][city[0]] == 0:
            continue
        for i in range(N-1):
            if W[city[i]][city[i+1]]==0:
                flag = False
                break
            sum += W[city[i]][city[i+1]]
        # if not flag:
        #     continue 
        if flag:
            sum += W[city[-1]][city[0]]
            currMin = min(sum, currMin)
    print(currMin)
dfs()