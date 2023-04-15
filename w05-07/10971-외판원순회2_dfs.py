import sys
from itertools import permutations
input = sys.stdin.readline

N = int(input())
W = list(list(map(int, input().split())) for _ in range(N))

currMin = 1e9