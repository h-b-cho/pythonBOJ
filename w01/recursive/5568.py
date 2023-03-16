import sys
input = sys.stdin.readline
N = int(input().strip())
K = int(input().strip())
cards = []
for _ in range(N): 
    cards.append(str(input().strip()))

# 정답 02 순열 구현 - 재귀함수 사용
arr = [0]*N
num = ''
tmp = ''
result = set()

def permu(n): 
    global num 
    if n==K:
        result.add(num) 
        return
    for i in range(N):
        if arr[i]==0:
            arr[i] = 1
            tmp = cards[i]
            num += tmp
            permu(n+1)
            arr[i] = 0
            num = num[:-len(tmp)]

permu(0)
print(len(result))




# # 정답 01 순열 라이브러리
# numlst = []
# for t in permutations(cards, K):
# 	num = ''.join(t)
# 	numlst.append(num)
# print(len(set(numlst)))