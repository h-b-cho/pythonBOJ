import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
  arr.append(int(input()))

for i in sorted(arr):
  print(i)

# import sys
# input = sys.stdin.readline
# N = int(input())
# arr = []
# for _ in range(N):
#     arr.append(int(input()))
# arrsorted = sorted(arr)
# for arritem in arrsorted:
#     print(arritem)