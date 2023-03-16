# import sys
# read = sys.stdin.readline

# n = int(read())

# for i in range(n):
#     print("*"*(i+1))

import sys
input = sys.stdin.readline

N = int(input())

for i in range(N):
    for _ in range(i + 1):
        print('*', end='')
    print()

#https://infinitt.tistory.com/11