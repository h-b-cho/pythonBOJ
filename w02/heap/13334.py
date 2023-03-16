import sys
import heapq
input = sys.stdin.readline
N = int(input())
HO = []
for _ in range(N):
    HO.append(sorted(list(map(int, input().split()))))
D = int(input())
HOh = []
for i in range(N):
    heapq.heappush(HOh, HO[i])
# print(HOh) # HO는 이제 HOh이라는 이름의 힙이 되었다.

heap = []
for ho in HO: # ho == [start, end]
    if abs(ho[1]-ho[0]) <= D:
        heapq.heappush(heap, ho)
# heap에 1차적으로 거른 후보군을 넣는다. 집-사무실 거리가 D보다 먼 항목들은 선상 어디에 위치해도 D안에 못 들어오니까 먼저 거른 것.

# heap.sort() # WRONG!!! end값을 기준으로 정렬해야 한다!!!
heap.sort(key=lambda x : x[1])

cnt = 0
tmph = []
for ho in heap: # 이제 heap의 요소들을 하나하나 검열할 거다. 
    if not tmph:
        heapq.heappush(tmph, ho) # 1. 가장 먼저, heap의 요소를 tmph에 넣는다.
    else:
        while tmph[0][0] < ho[1] - D: # 2. s<=e-D == true면 후보군에서 pop된다.
        # heap 요소의 e를 기준으로, 현재 heap의 루트의 s가 ("heap의 첫번째 요소의 e" - D)보다 작거나 같은지 확인.
        # 말인즉 D의 위치가 heap의 첫번째 요소의 e에서 끝난단 가정하에, s가 D 안에 있는지 보는 거다.
            heapq.heappop(tmph) # 3-2. 만약 true면 tmph에서 뺀다. tmph의 루트를 바로 그 다음 요소로 갈아끼우는 것.
            if not tmph: # 5. tmph가 비로소 빈 힙이 되면 for문 종료.
                break
        heapq.heappush(tmph, ho) # 3-1. 만약 s<=e-D == false면 tmph에 넣는다.
    cnt = max(cnt, len(tmph)) # 4. 그런 식으로 tmph의 길이가 얼마까지 최대로 늘어나나를 측정하는 것!

print(cnt)