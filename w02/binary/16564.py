import sys
input = sys.stdin.readline
N, K = input().split()
N = int(N)
K = int(K)
levels = [int(input()) for _ in range(N)]
levels = sorted(levels)

T = int(1e9)
start = 0
end = max(levels)+K # 탐색 범위의 최대값은 현재 가장 높은 레벨 + 올릴 수 있는 레벨인 k로 설정한다. 현재 가장 높은 레벨로 설정하면 안된다. 이미 젤 높은 레벨에도 값이 더해질 수 있으니까!

while start<=end:
    mid = (start+end)//2
    tmpsum = 0
    for level in levels:
        if level <= mid:
            tmpsum += int(mid)-int(level)
    if tmpsum <= K:
        T = mid
        start = mid+1
    else:
        end = mid-1
print(T)