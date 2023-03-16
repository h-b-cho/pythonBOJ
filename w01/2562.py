import sys
input = sys.stdin.readline

# 정답
arr = []
for _ in range(9):
    arr.append(int(input()))

# 오답
# arr = list(map(int, input().split()))

print( max(arr) )
print( arr.index(max(arr))+1 )