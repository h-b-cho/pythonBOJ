import sys
input = sys.stdin.readline
line = input().split('-')

num = []
for i in line:
    tmpsum = 0
    tmp = i.split('+')
    for j in tmp:
        tmpsum += int(j)
    num.append(tmpsum)

n = num[0]

for i in num[1:]:
    n -= i

print(n)