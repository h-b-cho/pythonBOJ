# 정답
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
coins = []
for _ in range(N):
	c = int(input())
	coins.append(c)

price = K
cnt = 0

for i in range(len(coins)):
    curr_coin = coins[len(coins)-i-1]
    while price//curr_coin >= 1:
        cnt += price//curr_coin
        price -= (price//curr_coin)*curr_coin
        if price==0:
            break

print(cnt)

# 시간초과
# import sys
# input = sys.stdin.readline
# N, K = map(int, input().split())
# coins = []
# for _ in range(N):
# 	c = int(input())
# 	coins.append(c)

# price = K
# count = 0

# for i in range(len(coins)):
#     curr_coin = coins[len(coins)-i-1]
#     while price//curr_coin >= 1:
#         price -= curr_coin
#         count += 1
#         if price==0:
#             break

# print(count)