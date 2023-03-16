# # 01 
# import sys
# import heapq
# input = sys.stdin.readline
# N = int(input())
# cards = list(int(input()) for _ in range(N))
# h = []
# tmph = []
# tmp0 = 0
# tot = 0 
# for c in cards:
#     heapq.heappush(h, c)

# for i in range(len(h)): heapq.heappush(tmph, h[i])
# # 힙 tmph은 현재 힙 h과 동일한 힙이다.

# while len(tmph)>1:
#     if N==1:
#         tot = 0
#         break
#     try:
#         if int(len(h))==N:
#             tmp1 = heapq.heappop(h)
#             tmp2 = heapq.heappop(h)
#             tot += tmp1+tmp2
#             heapq.heappop(tmph)
#             heapq.heappop(tmph)
#             heapq.heappush(tmph, tmp1+tmp2)
#         tmp1 = heapq.heappop(tmph)
#         tmp2 = heapq.heappop(tmph)
#         tmp0 = tmp1+tmp2
#         heapq.heappush(tmph, tmp0)
#         tot += tmp0
#     except:
#         if tmph==[]:
#             tot += tmp0+tmp1
#             break
# print(tot)

# 02
import sys
import heapq
input = sys.stdin.readline
N = int(input())
cards = list(int(input()) for _ in range(N))

heapq.heapify(cards)
tot = 0

while len(cards) > 1:
    tmp = heapq.heappop(cards) + heapq.heappop(cards)
    heapq.heappush(cards, tmp)
    tot += tmp

print(tot)