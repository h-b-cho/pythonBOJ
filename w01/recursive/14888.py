import sys
input = sys.stdin.readline

def dfs(depth, total, plus, minus, multiply, divide):   # total 파라미터는 A 배열에 있는 수들을 누적(by 재귀) 계산하기 위한 것
    global _max, _min
    
    if depth == N:
        _max = max(total, _max)
        _min = min(total, _min)
    
    if plus: 
        print('+')
        dfs(depth + 1, total + A[depth], plus - 1, minus, multiply, divide)
    if minus:
        print('-')
        dfs(depth + 1, total - A[depth], plus, minus - 1, multiply, divide)
    if multiply:
        print('*')
        dfs(depth + 1, total * A[depth], plus, minus, multiply - 1, divide)
    if divide:
        print('/')
        dfs(depth + 1, int(total / A[depth]), plus, minus, multiply, divide - 1)    # 문제 조건대로 나눗셈 설계

N = int(input())
A = list(map(int, input().split()))
plus, minus, multiply, divide = map(int, input().split())

_max = -1e9
_min = 1e9

dfs(1, A[0], plus, minus, multiply, divide)
print(_max)
print(_min)