import sys
input = sys.stdin.readline
N = int(input())
price = int(1000-N)
money = [500, 100, 50, 10, 5, 1]
cnt = 0
for i in money:
    while price//i >= 1 and price > 0:
        price-=i
        cnt += 1
print(cnt)