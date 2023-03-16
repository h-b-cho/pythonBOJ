# # 01
# import sys
# from itertools import combinations
# input = sys.stdin.readline

# arr = []
# arr.append(int(input()) for _ in range(9))

# for i in combinations(arr, 7): # 7명의 키 == 100인 경우를 찾는다.
# 	if sum(i)==100:
# 		ans = sorted(i)

# for ans_ in ans:
# 	print(ans_)

# 02
import sys
input = sys.stdin.readline

lst = []
for _ in range(9):
    lst.append(int(input()))

lst.sort()

sum_of_two = sum(lst)-100 # '7명의 키 합'==100인 경우는 '9명의 키 합'-100=='2명의 키 합' 인 경우를 찾는 것과 같다.

for i in range(0, 9):
    for j in range(1, 9):
        if lst[i] + lst[j] == sum_of_two:
            tar_i = i
            tar_j = j
            break

del lst[tar_i]
del lst[tar_j]
# lst.remove(lst[tar_i])
# lst.remove(lst[tar_j])

print(lst)