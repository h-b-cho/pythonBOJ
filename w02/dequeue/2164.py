from collections import deque
import sys  
input = sys.stdin.readline
N = int(input())

cards = deque([])
for i in range(1, N+1):
    cards.append(i)

while len(cards)>1:
    cards.popleft()
    n = cards.popleft()
    cards.append(n)
    
print(cards[0])