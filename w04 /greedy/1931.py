import sys
input = sys.stdin.readline
N = int(input())
time = [[] for _ in range(N) ]
for i in range(N):
	s, e = map(int, input().split())
	time[i].append(s)
	time[i].append(e)
time.sort(key=lambda x:(x[1], x[0])) # I have also added sorting by start time in addition to end time. This is important because if there are two meetings that end at the same time, you want to choose the one that starts earlier first.

end = 0
cnt = 0
for i in range(N):
    s = time[i][0]
    e = time[i][1]
    if s>=end:
        cnt += 1
        end = e

print(cnt)