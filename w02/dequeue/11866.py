from collections import deque
import sys  
input = sys.stdin.readline
N, K = input().split()
N = int(N)
K = int(K)
_i = 1
result = []

circle = deque([])
for i in range(1, N+1):
    circle.append(i)

# 답 01
while circle:
    for i in range(0, K-1):
        popl = circle.popleft()
        circle.append( str(popl) )
    result.append( str(circle.popleft()) )
    
answer = ", ".join(result)
print("<"+answer+">")

# # 답 02
# while circle:
#     popnl = circle.popleft()
#     if not circle:
#         result.append( str(popnl) )
#         break
#     if _i==K:
#         result.append( str(popnl) )
#         _i = 1
#         continue
#     circle.append( str(popnl) )
#     _i+=1

# answer = ", ".join(result)
# print("<"+answer+">")