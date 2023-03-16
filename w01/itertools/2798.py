import sys
from itertools import combinations
input = sys.stdin.readline

# N장의 카드에 써져 있는 숫자가 주어졌을 때, sum<M, sum이 최대이 경우의 카드 3장 조합을 구해 출력하시오.

N, M = map(int, input().split())
cards = list(map(int, input().split()))

# 오답
# arr = []
# cards = list(input().strip().split()) <--- string인 듯..
# for i in range(N):
#     arr.append(cards[i])

totalSum = -1e9

for c in combinations(cards, N):
	tempSum = sum(c)
	if tempSum>totalSum and tempSum<=M:
		totalSum=tempSum

print(totalSum)