import sys
input = sys.stdin.readline

T = int(input())
inplst = []
for _ in range(T):
    inplst.append(int(input()))
    
inpNSlsts = []

for inpN in inplst:  # === print([n*(n+1)//2 for n in range(1, 45)])
	S = 0
	p = 0
	inpNSlst=[]
	while S<=inpN:
		p+=1
		S+=p
		inpNSlst.append(S)
		if inpNSlst[-1]>inpN:
			inpNSlst.pop()
			inpNSlsts.append(list(inpNSlst))
			break
		else:
			continue

currSum = -1e9
ontable = list()
isS = 0

def findS(li, n, c, start):
	global isS

	if c==3:
		if sum(ontable)==n:
			isS = 1
			print(n, isS)
			return
		print(n, isS)
		return

	for start in range(start, len(li)):
		ontable.append(li[start])
		findS(li, n, c+1, start+1)
		ontable.pop()

findS(inpNSlsts[0], inplst[0], 0, 0)
findS(inpNSlsts[1], inplst[1], 0, 0)
findS(inpNSlsts[2], inplst[2], 0, 0)
