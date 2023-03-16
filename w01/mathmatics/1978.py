import sys
input = sys.stdin.readline

N = input()
ints = list(map(int, input().split()))
prime = 0

for n in ints:
    cnt = 0
    if n!=1:
        for i in range(2, n):
            if n%i==0:
                cnt+=1
        if cnt==0:
            prime+=1
print(prime)