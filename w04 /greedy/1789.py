# # 정답 - 1
# S = int(input())
# n = 1
# while n*(n+1)/2 <= S: # n*(n+1)/2는 1부터 n까지의 합의 공식이다.
#     n += 1
# print(n - 1)

# 잘못 접근한 오답 - 2
# import sys
# input = sys.stdin.readline
# S = int(input())
# s = S
# for i in range(1, S+1):
#     s -= i
#     if s < 0:
#         print(i-1)
#         break

# 정답 - 2
s = int(input())
total = 0
count = 0

while True:
    count += 1
    total += count
    if total > s:
        break

print(count-1)