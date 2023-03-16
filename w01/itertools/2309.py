import sys
from itertools import combinations
input = sys.stdin.readline
arr = []
for _ in range(9):
  arr.append(int(input()))

# 01
finish = False
for i in range(8):                      # 0~7   
    for j in range(i+1, 9):             # 1~8   
        if (arr[i]+arr[j] == sum-100):  #       
            save = [i, j]
            finish = True
            break
 
    if (finish):
        break

# 02
# for i in combinations(arr, 7): # 7명의 키 == 100인 경우를 찾는다.
# 	if sum(i)==100:
# 		ans = sorted(i)

# for ans_ in ans:
# 	print(ans_)