import sys
read = sys.stdin.readline

a = int(read())
b = int(read())

print(a * (b%10))
print(a * ((b//10)%10))
print(a * (b//100))
print(a * b)

# 테스트를 위해 콘솔에 입력값 input 시, "472_385" 이렇게 한 줄로 잘못 입력 -> string으로 감지되어 계속 valueError 오류났던