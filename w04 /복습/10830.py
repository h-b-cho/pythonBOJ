import sys
input = sys.stdin.readline
N, B = map(int, input().split())
A = [ list(map(int, input().split())) for _ in range(N) ]


def mul(matrix1, matrix2):
    n = len(matrix1)
    arr = [ [0 for _ in range(N)] for _ in range(N) ]
    for r in range(n):
        for c in range(n):
            sum = 0
            for i in range(n):
                sum += matrix1[r][i] * matrix2[i][c]
                arr[r][c] = sum%1000
    return arr

def square(a, b):
    if b==1:
        for x in range(len(a)):
            for y in range(len(a)):
                a[x][y] %= 1000
        return a
    tmp = square(a, b//2)
    tmp = mul(tmp, tmp)
    if b%2==0:
        return tmp
    else:
        return mul(tmp, a)

result = square(A, B)
for r in result:
    print(*r)