# from itertools import combinations
# arr = []

# def inp(n):
#   while input is not int:
#     S = list(map(int, input().split()))
#     arr.append(S)
    
#     if S==[0]:
#       S.pop()
      
#       for i in range(len(arr)):
#         for com in combinations(S[i], int(S[i][0])):
#           print(set(com))
#           print('')
#       exit()
      
#     else:
#       continue
# inp(0)


import sys
from itertools import combinations
input = sys.stdin.readline

def lotto(arr):
	for i in combinations(arr, 6):
		print(' '.join(map(str, i)))
	print()

while True:
	line = list(map(int, input().split()))
	if line[0]==0:
		break
	k = line[0]
	S = line[1:]
	lotto(S)