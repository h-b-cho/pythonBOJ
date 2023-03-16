# # 1. 시간초과
# import sys
# import heapq
# input = sys.stdin.readline
# N = int(input())
# heap = []
# for _ in range(N):
#     heapq.heappush(heap, int(input()))
#     tli = []
#     for _ in range((len(heap)-1)//2):
#         t = heapq.heappop(heap)
#         tli.append(t)
#     l = heapq.heappop(heap)
#     print( l )
#     for tl in tli:
#         heapq.heappush(heap, tl)
#     heapq.heappush(heap, l)

# 2. max heap 과 min heap 을 둘 다 사용
import sys
import heapq
input = sys.stdin.readline

N = int(input())
max_h, min_h = [], []

for i in range(N):
    num = int(input())
    
    if len(max_h) == len(min_h):
        heapq.heappush(max_h, -num)
    else:
        heapq.heappush(min_h, num)

    if len(max_h)>=1 and len(min_h)>=1 and max_h[0]*-1>min_h[0]:
        tar_max_value = heapq.heappop(max_h) * -1
        tar_min_value = heapq.heappop(min_h)
        heapq.heappush(max_h, tar_min_value * -1)
        heapq.heappush(min_h, tar_max_value)

    print(max_h[0] * -1)