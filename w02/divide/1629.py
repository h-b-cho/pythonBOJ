import sys 
input = sys.stdin.readline
A, B, C = input().split()
A = int(A)
B = int(B)
C = int(C)

def dac(a, b, c):
    if b==1:
        return a % c               # (a**1)%c
    temp = dac(a, b//2, c)
    if b%2==0:
        return temp * temp % c     # (a**b//2)*(a**b//2)%c
    else:
        return temp * temp * a % c # (a**b//2)*(a**b//2)*a%c

print(dac(A, B, C))