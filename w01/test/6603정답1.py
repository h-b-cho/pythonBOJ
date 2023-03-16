# # 1 - 백트래킹
# def get_combinations(com, S):
#     if len(com) == 6:
#         print(" ".join(com))
#         return
#     start = S.index(com[-1]) + 1 if com else 0
#     for i in range(start, len(S)):
#         get_combinations(com + [S[i]], S)

# while 1:
#     N = input().split()
#     if N[0] == "0":
#         break
#     get_combinations([], N[1:])
#     print()

# 2 - itertools
from itertools import combinations
while 1:
    N = input().split()
    # print(N)
    if N[0]=="0":
        break
    S = N[1:]
    
    for c in combinations(S, 6):
        print(" ".join(c))
    print()