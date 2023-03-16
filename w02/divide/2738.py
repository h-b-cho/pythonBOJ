import sys
input = sys.stdin.readline
N, M = map(int, input().split())
A = []
B = []
for row in range(N):
    row = list(map(int, input().split()))
    A.append(row)
for col in range(N): # M이 아니다.
    col = list(map(int, input().split()))
    B.append(col)

for r in range(N):
    row = ''
    for c in range(M):
        row += (str(A[r][c] + B[r][c])+' ')
    print(row)