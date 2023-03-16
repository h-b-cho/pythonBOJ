### 정답안 열람한 뒤 참고하여 풀이.

import sys
import heapq
input = sys.stdin.readline
K, N = input().split()
K = int(K)
N = int(N)
nums = list(map(int, input().split()))
sums = []

for n in nums:
    heapq.heappush(sums, n)

num = 0

for _ in range(N):
    num = heapq.heappop(sums)
    for j in range(K):
        tmp = num*nums[j]
        heapq.heappush(sums, tmp)
        if num%nums[j]==0:
            break
print(num)