import sys
import heapq
input = sys.stdin.readline
N = int(input())
heap = []

for _ in range(N):
    num = int(input())
    if num==0:
        try:
            print(-1, heapq.heappop(heap))
        except:
            print(0)
    else:
        heapq.heappush(heap, -num)
        
        
    # if num==0:
    #     try:
    #         print(-1 * heapq.heappop(heap)) # 2. 입력값으로 0이 들어왔을 때에 현재 마이너스화 된 heap 요소 중 가장 작은, 
    #                                         # 즉 현재 heap의 요소 중 절대값이 가장 큰 것을 다시 양수화해서 heapq.heappop() --> 그것을 print()한다.
    #     except:
    #         print(0)
    # else:
    #     heapq.heappush(heap, -num) # 1. 모든 입력값 num을 차례대로 마이너스화 해서 변수 heap에 heapq.heappush()한다.