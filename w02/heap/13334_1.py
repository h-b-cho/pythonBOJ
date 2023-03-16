import sys
import heapq
n = int(sys.stdin.readline())
road_info = []
for _ in range(n):
    road = list(map(int, sys.stdin.readline().split()))
    road_info.append(road)
d = int(sys.stdin.readline())


heap = []
for road in road_info:
    house, office = road
    if abs(house - office) <= d:
        road = sorted(road)
        heap.append(road)
        
heap.sort(key=lambda x:x[1])

answer = 0
tmph = []
for ho in heap:
    if not tmph:
        heapq.heappush(tmph, ho)
    else:
        while tmph[0][0] < ho[1] - d:
            heapq.heappop(tmph)
            if not tmph:
                break
        heapq.heappush(tmph, ho)
    answer = max(answer, len(tmph))

print(answer)