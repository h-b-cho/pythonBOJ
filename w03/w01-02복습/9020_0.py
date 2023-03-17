import sys
from itertools import combinations
input = sys.stdin.readline
T = int(input())
numbers = list(int(input()) for _ in range(T))

primes = []
for i in range(2, 10001):
    for j in range(2, i):   # n**0.5 의 개념을 까먹음!
        if i%j==0:
            break
    else:
        primes.append(i)

### 오답
### input 넣어도 작동하지 않음
result = []
for n in numbers:
    tmpprimes = []
    for p in primes:   
        while p<=n:
            tmpprimes.append(p)
    for p in combinations(tmpprimes, 2):
        if n==sum(p):
            result.append(p)
            break

print(result)

