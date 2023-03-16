import sys
input = sys.stdin.readline
N = int(input())

def iHanoiYou(N):
    K = 2**N-1
    def Hanoi(N, start, to, via):
        if N==1:
            print(start, to)
        else:
            Hanoi(N-1, start, via, to)
            print(start, to)
            Hanoi(N-1, via, to, start)
    print(K)
    if N <= 20:
        Hanoi(N, 1, 3, 2)
iHanoiYou(N)



# 하노이 외우기..
# def 하노이(n s t v):
#     if input==1:
#         움직임(s t)
#     else:
#         하노이(n-1 s v t)
#         print(s t)||움직임(s t)
#         하노이(n-1 v t s)


#-----------------------

# import sys
# input = sys.stdin.readline
# N = int(input())

# def solution(N):
#     K = 2**N-1
#     def Hanoi(N, s, t): # 시작기둥 s번와 목표기둥 t번이 할 시, 자동으로 보조기둥의 번호는 1+2+3-s-t이 된다.
#         if N>1:
#             Hanoi(N-1, s, 6-s-t)
#         print(f'{s} {6-s-t}')
#         if N>1:
#             Hanoi(N-1, 6-s-t, t)
    
#     if N>20:
#         print(K)
#     else:
#         print(K)
#         Hanoi(N, 1, 3)

# solution(N)