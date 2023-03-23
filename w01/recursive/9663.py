# 1. 8*8 격자판에서 각 열에 퀸을 1개씩 배치하는 조합을 모두 프린트
pos = [0]*8

def put()->None:
    for i in range(8):
        print(f'{pos[i]:2}', end="")
    print()
    
def set(n:int)->None:
    for j in range(8):
        pos[n] = j
        if n==7:
            put()
        else:
            set(n+1)

set(0)

# 2. 8*8 격자판에서 각 열에 퀸을 1개씩 배치하는 조합 중 이미 퀸이 배치된 열에 flag를 꽂아 열이 겹치치 않게 배치하는 조합을 모두 프린트
pos = [0]*8
flag = [False]*8

def put()->None:
    for i in range(8):
        print(f'{pos[i]:2}', end="")
    print()
    
def set(n:int)->None:
    for j in range(8):
        if not flag[j]:
            pos[n] = j
            if n==7:
                put()
            else:
                flag[j] = True
                set(n+1)
                flag[j] = False

set(0)

# 3. 8*8 격자판에서 이미 퀸이 1개 놓인 열, 행, 대각선에 flag를 꽂아 그 열, 행, 대각선에 다른 퀸이 겹치치 않게 배치하는 조합을 모두 프린트
pos = [0]*8
flag_a = [False]*8
flag_b = [False]*15
flag_c = [False]*15

def put():
    for i in range(8):
        print(f'{pos[i]:2}', end="")
    print()
    
def set(n:int):
    for j in range(8):
        if ( not flag_a[j]
            and not flag_b[n+j]
            and not flag_c[n-j+7] ):
            pos[n] = j
            if n==7:
                put()
            else:
                flag_a[j] = flag_b[n+j] = flag_c[n-j+7] = True
                set(n+1)
                flag_a[j] = flag_b[n+j] = flag_c[n-j+7] = False

set(0)

# 4. 위를 입력값 N에 따른 N*N 격자판 버전으로
import sys  
input = sys.stdin.readline
N = int(input())
pos = [0]*N
flag_a = [False]*N
flag_b = [False]*(N*2-1)
flag_c = [False]*(N*2-1)

def put(end):
    for i in range(end):
        print(f'{pos[i]:2}', end="")
    print()
    
def set(n, end):
    for j in range(end):
        if ( not flag_a[j]
            and not flag_b[n+j]
            and not flag_c[n-j+end-1] ):
            pos[n] = j
            if n==end-1:
                put(end)
            else:
                flag_a[j] = flag_b[n+j] = flag_c[n-j+end-1] = True
                set(n+1, end)
                flag_a[j] = flag_b[n+j] = flag_c[n-j+end-1] = False

set(0, N)

# 5. 경우의 수 count를 프린트
import sys  
input = sys.stdin.readline
N = int(input())
pos = [0]*N
flag_a = [False]*N
flag_b = [False]*(N*2-1)
flag_c = [False]*(N*2-1)
count = 0

def set(n, end):
    global count
    for j in range(end):
        if ( not flag_a[j]
            and not flag_b[n+j]
            and not flag_c[n-j+end-1] ):
            pos[n] = j
            if n==end-1:
                count+=1
            else:
                flag_a[j] = flag_b[n+j] = flag_c[n-j+end-1] = True
                set(n+1, end)
                flag_a[j] = flag_b[n+j] = flag_c[n-j+end-1] = False
    return count

print(set(0, N))