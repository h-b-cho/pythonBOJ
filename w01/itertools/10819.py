import sys
from itertools import permutations
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

x = 0
cases = list(permutations(arr))

for case in cases:
	temp_sum = 0
	for i in range(N-1):
		temp_sum+=abs(case[i]-case[i+1])
		if x<temp_sum:
			x = temp_sum

print(x)


# import sys
# from itertools import permutations
# input = sys.stdin.readline
# isMax = 0
# N = int(input())
# lst = list(map(int, input().split()))

# for set in list(permutations(lst)):
#     setSum = 0
#     for i in range(N-1):
#         setSum += abs(set[i]-set[i+1])
#     if setSum>isMax:
#         isMax=setSum
# print(isMax)
