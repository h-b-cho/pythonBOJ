import sys
input = sys.stdin.readline
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
blue = 0
white = 0

def recur(x, y, N) :
    global white, blue
    color = board[x][y]
    for i in range(x, x+N) :
        for j in range(y, y+N) :
            if color != board[i][j] :
                recur(x,      y,      N//2) # 1사분면
                recur(x,      y+N//2, N//2) # 2사분면
                recur(x+N//2, y,      N//2) # 3사분면
                recur(x+N//2, y+N//2, N//2) # 4사분면
                return
    if color==0 :
        white+= 1
    else :
        blue+= 1

recur(0, 0, N)
print(white, blue, sep='\n')