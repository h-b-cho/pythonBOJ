import sys  
input = sys.stdin.readline
K = int(input())
stack = []
nums = list(int(input()) for i in range(K))
for num in nums:
  if num!=0:
    stack.append(num)
  else:
    stack = stack[:-1]
  
print(sum(stack))