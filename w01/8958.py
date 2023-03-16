import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    total = 0
    plus = 0
    inp = input().strip() #개행문자삭제
    for j in inp:
        if j == "X":
            plus = 0
        else:
            plus += 1
        total += plus

    print(int(total))

# https://mgyo.tistory.com/166