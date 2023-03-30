import sys
import heapq
from collections import deque

input = sys.stdin.readline

n = int(input())

# 빈 강의실을 담아둘 Queue
room = deque()
room.append(1)

k = 1  # 현재 사용하고 있는 강의실의 개수
lecture = []
result = [0] * (n+1)

for _ in range(n):
    num, start, end = map(int, input().split())
    lecture.append((start, end, num))

# 강의들을 시작 시간을 기준으로 정렬
lecture.sort()
h = []

for i in range(n):
    start, end, num = lecture[i]

    # 현재 강의의 시작 시점에서 이미 끝난 강의들을 빼준다
    while h and start >= h[0][0]:
        # 강의를 빼줄때 할당되어있던 강의실을 빈 강의실로 분류
        room.append(heapq.heappop(h)[1])
    if room:
        # 빈 강의실이 남아있으면 그거 할당
        room_num = room.popleft()
        result[num] = room_num
        heapq.heappush(h, (end, room_num))
    else:
        # 빈 강의실이 없으면 새로 만들어서 할당
        k += 1
        heapq.heappush(h, (end, k))
        result[num] = k

print(k)
for i in range(1, n+1):
    print(result[i])