
import sys
import heapq
N = int(input())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
arr.sort(key=lambda x: (x[1], x[2]))  # 정렬 1순위: 시작순, 2순위: 종료순

using_room = []  # 사용중인 강의실 (끝나는 시간, 방 번호)
empty_room = []  # 빈 강의실

for i in range(1, N+1):
    heapq.heappush(empty_room, i)  # 빈 방 번호 1부터 N으로 초기화

result = [0] * (N+1)  # result[강의 번호] = 강의실 번호

for i in range(N):
    lecture_num, start, end = arr[i]

    while using_room and using_room[0][0] <= start:  # 이미 끝난 강의라면
        end_time, room_num = heapq.heappop(using_room)  # 사용하던 강의실 가져와서
        heapq.heappush(empty_room, room_num)  # 빈 강의실로 변경

    empty_room_num = heapq.heappop(empty_room)  # 빈 강의실 중 제일 낮은 번호 가져오기
    heapq.heappush(using_room, [end, empty_room_num])  # 현재 강의의 강의실로 배정
    result[lecture_num] = empty_room_num

print(max(result))
for r in result[1:]:
    print(r)