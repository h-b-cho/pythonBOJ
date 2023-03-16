import sys
input = sys.stdin.readline
men = [int(input()) for _ in range(9)]
arr = []

# def dfs(depth, start):
#     if depth==7:
#         if sum(arr)==100:
#             arrset = sorted(arr)
#             for a in arrset:
#                 print(a)
#             exit()
#         return   # 만약 7명을 뽑았는데 합이 100이 아니라면 해당 재귀를 더 이상 실행하지 않고 종료

#     for i in range(start, len(men)): 
#         arr.append(men[i])
#         dfs(depth+1, i+1)  # dfs를 돈다(다음 번 깊이는 +1로 해주고 인덱스는 중복되지 않게 하기 위해 다음 인덱스를 넣어준다.)
#         arr.pop()          # dfs를 돌다 7명이 다 찼으나 합이 100이 아니어서 return 되었으면 넣었던 난쟁이 한명을 다시 빼준다.

# dfs(0, 0)

def dfs(start, cnt):
    if cnt==7:
        if sum(arr)==100:
            arrset = sorted(arr)
            for a in arrset:
                print(a)
            exit()
        # return # 오답 - 위의 dfs()와 이 dfs()의 차이는, 받는 인자의 순서가 다른 점이라 할 수 있다. 여기서 이 위치의 return이 유무를 달리한다.
    
    for i in range(start, len(men)):
        arr.append(men[i])
        dfs(start+1, cnt+1)
        arr.pop()

dfs(0, 0)