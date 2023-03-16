# 소수 구하기
# from math import sqrt
def is_prime(n):
    if n==1: # 1은 무조건 false.
        return False
    for j in range(2, int(n**0.5)+1): # range(2, n**0.5) 사이에 있는 숫자로 나누어 떨어지면 false. int(n**0.5) == int(sqrt(n)) 이니까.
        if n%j==0:
            return False
    return True

def isPrime(x):
  if x==1:
      return False
  for j in range(2, int(x**0.5)+1):
    if x%j==0:
      return False
  return True