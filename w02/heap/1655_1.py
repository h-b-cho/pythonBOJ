# 시간 초과
import heapq
import sys
n = int(sys.stdin.readline())
baekjoon = [int(sys.stdin.readline()) for _ in range(n)]
# heap = heapq.heapify(baekjoon)
heap = []
res = []
for i in range(1, n+1):
    for j in range(i):
        heapq.heappush(heap, baekjoon[j])
    for k in range((len(heap)-1) //2):
        heapq.heappop(heap)
    print(heapq.heappop(heap))
    while heap:
        heapq.heappop(heap)

# 다시
import heapq
import sys
input = sys.stdin.readline
N = int(input())
max_heap = []  # -> len(min_heap) + 1
min_heap = []  #
medians  = []
for _ in range(N):
    num = int(input())
    if len(min_heap) == len(max_heap):
        heapq.heappush(max_heap, (-num, num))
    else:
        heapq.heappush(min_heap, (num, num))
    if min_heap and max_heap[0][1] > min_heap[0][1]:
        temp1 = max_heap[0][1]
        temp2 = min_heap[0][1]
        heapq.heappop(min_heap)
        heapq.heappop(max_heap)
        heapq.heappush(min_heap, (temp1, temp1))
        heapq.heappush(max_heap, (-temp2, temp2))
    medians.append(max_heap[0][1])
for median in medians:
    print(median)