### 정답
import sys 
input = sys.stdin.readline
N = int(input())
tower = list(map(int, input().split()))
stack = []
answer = []

for i in range(N):
    while stack:
        if stack[-1][1] > tower[i]:
            answer.append(stack[-1][0]+1)
            break
        else:
            stack.pop()
    if not stack:
        answer.append(0)
    stack.append([i, tower[i]])

print(" ".join(map(str, answer)))



### -------------------------------------



### 시간초과
# import sys 
# input = sys.stdin.readline
# N = int(input())
# tower = list(map(int, input().split()))

# towerstack = []
# for i in range(N):
#     towerstack.append([i, tower[i]])

# answer = ''

# for i in range(N):
#     stack = towerstack.copy()[:i]
#     if i==0:
#         answer += str(0)+' '
#     else:
#         while stack:
#             if stack[-1][1] > tower[i]:
#                 answer += str(stack[-1][0]+1)+' '
#                 break
#             else:
#                 stack.pop()
#             if not stack:
#                 answer += str(0)+' '

# print(answer)