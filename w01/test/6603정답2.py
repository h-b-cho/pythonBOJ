from itertools import combinations

while True:
    temp_arr = input()

    if temp_arr == '0':
        break 

    N = int(temp_arr[0])
    arr = list(map(int,temp_arr.split(' ')))[1:]

    for result in combinations(arr,6):
        print(*result)
    print()

# 백트래킹
def dfs(next,cnt,visited):
    if cnt == 6:
        print(*visited)
        return
    for i in range(next,len(arr)):
        visited.append(arr[i])
        dfs(i+1,cnt+1,visited)
        visited.pop()

while True:
    temp = list(map(int,input().split()))
    N = temp[0]
    arr = temp[1:]
    if N==0:
        break