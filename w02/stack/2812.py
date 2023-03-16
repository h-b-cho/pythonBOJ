import sys
input = sys.stdin.readline
N, K = map(int, input().split())
number = list(map(int, input().strip()))

stack = []

for i in range(N):
    while K>0 and stack and stack[-1]<number[i]:
        stack.pop()
        K-=1
    stack.append(number[i])

result = ''
for n in stack[:len(stack)-K]:
    result += str(n)

print(result) 