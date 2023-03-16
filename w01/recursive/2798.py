import sys
input = sys.stdin.readline

currMax = -1e9
ontable = list()

def recur(c, start):
    global currMax
    
    if c==3:
        if sum(ontable)>currMax and sum(ontable)<=M:
            currMax = sum(ontable)
        return
    for start in range(start, N):
        ontable.append(int(cards[start]))
        recur(c+1, start+1)
        ontable.pop()

N, M = map(int, input().split())
cards = list(map(int, input().split()))

recur(0, 0)
print(currMax)