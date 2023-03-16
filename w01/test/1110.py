import sys
input = sys.stdin.readline

N = int(input())
num = 0
cnt = 0

def recur(n):
	global cnt
	global num
	while True:
		if n==0:
			print(1)
			exit()
		if num==N:
			print(cnt)
			exit()
		cnt+=1
		a = n//10
		b = n%10
		c = (a+b)%10
		num = (b*10)+c
		recur(num)

recur(N)