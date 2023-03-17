# # 01
import sys
from itertools import permutations
input = sys.stdin.readline
N = int(input())
K = int(input())
cards = list(str(input()) for _ in range(N)) # int()가 아님! 밑에서 ''.join() 할거라
numbers = []

for t in permutations(cards, K):
	num = ''.join(t)
	numbers.append(num)
	
print(len(set(numbers)))

# 02
import sys
input = sys.stdin.readline
N = int(input())
K = int(input())
cards = list(str(input()).strip() for _ in range(N)) # 오답: strip() 빼먹음-_-

numberset = set()
arr = [0]*N
number = ''

def permu(n):
    global number
    if n==K:
        numberset.add(number)
        return
    for i in range(N):
        if arr[i]==0:       # 오답: if문을 빼먹음-_- 장난?
            arr[i] = 1
            tmp = cards[i]
            number += tmp
            permu(n+1)
            arr[i] = 0
            number = number[:-len(tmp)] # 오답: number[:-len(str(i))]
permu(0)
print(len(numberset))