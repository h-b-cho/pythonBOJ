import sys
input = sys.stdin.readline
N = int(input())

f = [0, 1]

if N==0:
    print(f[0])
else: 
    for n in range(1, N):
        f.append(f[n]+f[n-1])
    print(f[-1])