import sys
input = sys.stdin.readline
N, B = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

# 행렬 곱셈할 조합 만들기
def comb(n, matrix1, matrix2):
    result = [[0 for _ in range(n)] for _ in range(n)]

    for r in range(n):
        for c in range(n):
            for i in range(n):
                result[r][c] += (matrix1[r][i] * matrix2[i][c]) % 1000

    return result

# 먼지가 될 때까지 2분할
def devide(n, b, matrix):
    if b==1:
        return matrix
    elif b==2:
        return comb(n, matrix, matrix)
    else:
        tmp = devide(n, b//2, matrix)
        if b%2==0:
            return comb(n, tmp, tmp)
        else:
            return comb(n, comb(n, tmp, tmp), matrix)

result = devide(N, B, A)

for row in result:
    for num in row:
        print(num%1000, end=' ')
    print()