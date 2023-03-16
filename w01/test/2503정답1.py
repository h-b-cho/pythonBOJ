# # 1 - 백트래킹
# import sys

# # 순열 구하는 함수
# permu_list= []
# def get_permutations(permu, used):
#     global permu_list
#     if len(permu) == 3:
#         permu_list.append(permu)
#         return
#     [get_permutations(permu + str(i), used+[i]) for i in range(1,10) if i not in used]
# get_permutations("", [])

# # 해당 케이스에 가능한 숫자 탐색
# def get_results(guess, results):
#     can = []
#     for p in permu_list:
#         strike = sum(p[i] == guess[i] for i in range(3))
#         ball = sum(guess[i] in p  for i in range(3)) - strike
#         if results == (strike, ball):
#             can += [p]
#     return can


# result = []
# for _ in range(int(input())):
#     guess, strike, ball = map(int,sys.stdin.readline().split())
#     can = get_results(str(guess), (strike, ball))
#     # 모든 케이스에 중복된 숫자만 남김
#     result = can if result == [] else [c for c in can if c in result]

# print(len(result))



# 2 - itertools
import sys
from itertools import permutations

def get_results(guess, results):
    can = []
    for p in permutations('123456789',3):
        strike = sum(p[i] == guess[i] for i in range(3))
        ball = sum(guess[i] in p  for i in range(3)) - strike
        if results == (strike, ball):
            can += [p]
    return can

result = []
for _ in range(int(input())):
    guess, strike, ball = map(int,sys.stdin.readline().split())
    can = get_results(str(guess), (strike, ball))
    result = can if result == [] else [c for c in can if c in result]

print(len(result))