import sys
import heapq
input = sys.stdin.readline
N = int(input())
time = [ [] for _ in range(N) ]
for i in range(N):
	n, s, e = map(int, input().split())
	time[i].append(n)
	time[i].append(s)
	time[i].append(e)
time.sort(key=lambda x:(x[1], x[2]))

### heapq 쓰면서 진행하던 사항

lecture = [0 for _ in range(N+1)]
room = []
for i in range(1, n+1):
    heapq.heappush(room, i)

minHeap = []
for curr in time:
    while minHeap and minHeap[0][0] <= curr[1]:
        end, r = heapq.heappop(minHeap)
        heapq.heappush(room, r)

    r = heapq.heappop(room)
    heapq.heappush(minHeap, [curr[2], r])
    lecture[curr[0]] = r

print(max(lecture))
for curr in lecture[1:]:
    print(curr)

### heapq 없이 진행하던 사항 (11행 = 36행)

# time.sort(key=lambda x:(x[2], x[1]))

# end = [time[0][2]]
# idx = [ [] for _ in range(N) ]
# idx[0] = time[0][0]
# cnt = 1

# for i in range(1, N):
#     s = time[i][1]
#     e = time[i][2]
#     for j in end:
#         if s>=j:
#             j = e
#             idx[time[i][0]] = len(end)
#             break
#     else:
#         end.append(e)
#         idx[time[i][0]] = len(end)