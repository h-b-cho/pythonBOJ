import sys
input = sys.stdin.readline

a, b, v = map(int, input().split())

# 풀이1
# import math
# print(math.ceil((v-b)/(a-b))) 

# 풀이2
# 낮에 도착하는 경우: (v-b)%(a-b)==0
if (v-b)%(a-b)==0:
    print((v-b)//(a-b))
else:
    print((v-b)//(a-b)+1)