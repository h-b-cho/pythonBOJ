# N = int(input())
# lst = [0, 1]

# def Fibo(N):
#   global lst
  
#   if N<=1:
#     print(lst[N])
#     return int(lst[N])
#   for i in range(N):
#     lst.append(lst[len(lst)-2]+lst[len(lst)-1])
#   print(lst[i+1])
#   return int(lst[i+1])

# Fibo(N)

N = int(input())

def Fibo(N):
	if N<=1:
		return N
	return Fibo(N-1)+Fibo(N-2)

print(Fibo(N))