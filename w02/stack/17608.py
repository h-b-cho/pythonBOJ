import sys  
input = sys.stdin.readline
N = int(input())
# stack = list(input().strip() for _ in range(N)) # wrong
stack = [int(input()) for _ in range(N)]
currMax = stack[-1]
count = 1
for h in stack[::-1]:
  if h > currMax:
    currMax = h
    count += 1

print(count)