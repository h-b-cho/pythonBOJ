N = int(input())

def Han(N: int):
	if N<100:
		return print(N)
	elif N==1000:
		return print(int(144))
	else:
		cnt = 99
		for i in range(101, N+1):
			Nlist = list(map(int, str(i)))
			if int(Nlist[0]-Nlist[1]) == int(Nlist[1]-Nlist[2]):
				cnt += 1
		return print(cnt)

Han(N)