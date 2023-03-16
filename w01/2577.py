import sys
input = sys.stdin.readline
a = int(input())
b = int(input())
c = int(input())

#01

numlst = list(str(a*b*c))
for i in range(0, 10):
	count = 0
	for n in numlst:
		if i==int(n):
			count+=1
	print(count)
	
#02

# abc = str(a*b*c)
# for i in range(0, 10):
#	 print(abc.count(str(i))) #array.count(item)