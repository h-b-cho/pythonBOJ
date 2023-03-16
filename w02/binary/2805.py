import sys  
input = sys.stdin.readline
N, M = input().split()
N = int(N)
M = int(M)
heights = list(map(int, input().split())) # len == N
result = 0

def tree_binary_search(srtarr, start, end):
    global result
    while start<=end:
        mid = (start+end)//2
        sum = 0
        for i in srtarr:
            if i > mid:
                sum += i-mid
        if sum < M:
            end = mid-1
        else:
            result = mid
            start = mid+1
    return result
    
print(tree_binary_search(heights, 0, max(heights)))