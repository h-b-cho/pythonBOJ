import sys
input = sys.stdin.readline
N = int(input())
board = list( list(map(int, input().split())) for _ in range(N) )
blue = 0
white = 0

def recur(x, y, N):
    global white, blue
    color = board[x][y]             # 현재 내가 들고있는 색깔(즉, 직전의 for문 때 확인한 색깔)
    for row in range(x, x+N):       # 처음 시작하는 종이의 가로 변: 0부터 N까지.
        for col in range(y, y+N):   # 처음 시작하는 종이의 세로 변: 0부터 N까지.
            check = board[row][col] # 지금(이번 for문) 확인할 종이칸 좌표. 뭔 색깔인지 확인. 
            if color != check:      # 색이 이어지지 않고 달라졌다면 잘라줄 것이다!
                recur(x, y, N//2)           # 1. 현재 종이의 1사분면으로 가 색깔 확인하는 수행. 
                recur(x, y+N//2, N//2)      # 3. 현재 종이의 2사분면으로 가 색깔 확인하는 수행. 
                recur(x+N//2, y, N//2)      # 5. 현재 종이의 3사분면으로 가 색깔 확인하는 수행. 
                recur(x+N//2, y+N//2, N//2) # 7. 현재 종이의 4사분면으로 가 색깔 확인하는 수행.
                # 9. 길이가 N//2이 되어 처음에서부터 4분할 된 종이 4개를 한 번 싹 돌았다. 이제 그것들을 길이가 N//2//2인 종이들로 한 번씩 더 난도질해서 총 16분할 된 종이들도 돌아가며 확인한다. 처음으로 올라서 아까처럼 recur() 4개를 쭉 훑고 내려올 것.
                return
    # 2. 4. 6. 8. 길이가 N//2이 된 사분면으로 가 한 바퀴 쭉 다 돌고 색깔 확인하는 수행을 마침.
    #             방금 내가 자른 종이가 무슨 색인지 확인 후 수 적립 후 다음 사분면으로 감.
    if color==0:
        white += 1
    else:
        blue += 1

recur(0, 0, N)
print(white, blue, sep='\n')