import sys
input = sys.stdin.readline
T = int(input())
nums = list(int(input()) for _ in range(T))

# def isPrime(x):
#   if x==1:
#       return False
#   for j in range(2, int(x**0.5)+1):
#     if x%j==0:
#       return False
#   return True

# for num in nums:
#     n1 = num//2
#     n2 = num//2
#     for _ in range(num//2):  
#       if isPrime(n1) and isPrime(n2):
#         print(f'{n1} {n2}') 
#         # print(int(n1), int(n2)) # 정답
#         break
#       else:
#         n1-=1
#         n2+=1

def isprime(x):
	for j in range(2, int(x**0.5)+1):
		if x%j==0: 
			return False
		# else: 
		# 	return # 오답 - 돌던 for문을 종료해버리고 나간다. 그러면 안 돼~
	return True

for num in nums:
	n1 = num//2
	n2 = num//2
	for _ in range(num//2):
		if isprime(n1) and isprime(n2):
			print(f'{n1} {n2}') 
			break
		else:
			n1-=1
			n2+=1