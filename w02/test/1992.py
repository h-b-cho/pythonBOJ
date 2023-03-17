### 정답안 열람한 뒤 참고하여 풀이하는 중...

import sys
input = sys.stdin.readline
N = int(input())
matrix = [list(map(str, input().split())) for _ in range(N)]
rows  = []
for c in range(len(matrix)):
    for r in range(len(matrix[c])):
        tmp = []
        tmp += (matrix[c][r])
        rows.append(tmp)

answer = ''

# print(matrix)

# for r in range(len(rows)):
#     for i in range(len(rows[r])):
#         target = (rows[r][i])
#             if rows[r][i-1]==rows[r][i]:

def recur(x, y, N):
    check = matrix[x][y]
    global answer
    for r in range(x, x + N):
        for c in range(y, y + N):
            if check != matrix[r][c]:
                recur(x,      y,      N//2) # 1사분면
                recur(x,      y+N//2, N//2) # 2사분면
                recur(x+N//2, y,      N//2) # 3사분면
                recur(x+N//2, y+N//2, N//2) # 4사분면
                return
    if check == '0':
        answer += '0'
    else:
        answer += '1'
    return

recur(0, 0, N)
print(answer)