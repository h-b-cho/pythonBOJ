T = int(input())

def recursion(s, a, z) -> int:
	global count
	count+=1
	if a>=z: 
		return 1
	elif s[a]!=s[z]: 
		return 0
	else: 
		return recursion(s, a+1, z-1)

def isPalindrome(s):
	return recursion(s, 0, len(s)-1)

for i in range(T):
	S = str(input())
	count = 0
	print(isPalindrome(S), count)