import sys
input = sys.stdin.readline

a, b = list(map(int, input().split()))

aa = ''.join(reversed(str(a)))
bb = ''.join(reversed(str(b)))

if int(aa)>int(bb):
  print(aa)
else: 
  print(bb)

# 1152번

# _string = list(map(str, input().split()))
# print(len(_string))