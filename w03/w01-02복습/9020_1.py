import sys
input = sys.stdin.readline
T = int(input())
numbers = list(int(input()) for _ in range(T))

def isPrime(n):
    for j in range(2, int(n**0.5)+1):
        if n%j==0:
            break
    else:
        return True

for num in numbers:
    n1 = num//2
    n2 = num//2
    for _ in range(num//2):
        if isPrime(n1) and isPrime(n2):
            print(f'{n1} {n2}') 
            break
        else:
            n1-=1
            n2+=1