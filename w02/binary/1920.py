N = int(input())
A = list(map(int, input().split()))
M = int(input())
arr = list(map(int, input().split()))
A.sort()

for num in arr:
    lt, rt = 0, N - 1
    isExist = False	

    while lt <= rt:
        mid = (lt+rt)//2
        if num == A[mid]:
            isExist = True
            print(1)
            break
        elif num > A[mid]:	# A[mid]가 num보다 작으면,
            lt = mid+1	    # lt를 +1 높여서 탐색범위 좁힘.
        else:			    # A[mid]가 num보다 크다면,
            rt = mid-1	    # rt를 -1 낮춰서 탐색범위 좁힘.

    if not isExist:
        print(0)