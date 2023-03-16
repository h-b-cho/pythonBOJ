# 입력이 공백으로 나뉜 한 줄짜리 입력값일 때, 빌트인input()
a = [int(x) for x in input().split()]

## input() 대신 --> map 과 sys.stdin.readline으로 정수의 map()의 list()화
import sys 
input = sys.stdin.readline
a = list(map(int, input().split()))

# -----------
# 다시 말하면, 입력을 공백으로 구분된 한 줄로 받을 때: 
lst = input().split() # 이걸 너무 늦게 알았다 하..
lst = list(map(int, input().split()))

# 여러 라인 입력받아야 할 경우:
a = int(input())
b = int(input())
c = int(input())

## 여러 라인 입력받아야 할 경우 - 문제 풀이 상 총 몇 줄의 입력값인지 고정적이며 그걸 리스트로 보관할 때:
arr = []
for _ in range(9): # 9줄 고정일 때
    num = int(input())
    arr.append(num)

arr = list(int(input()) for _ in range(9))

# 여러 라인 입력받아야 할 경우 - 입력값의 맨 앞에 테스트케이스의 갯수 주어질 때:
c = int(input())
for _ in range(c):
  arr = list(map(int, input().split()))
#
c = int(input())
arr = list(map(int, input().split()) for _ in range(c))

#
# sys.stdin.readline 끝에 \n은 rstrip()으로 없앨 수 있다(값 스트링화 됨)

# 17608
# stack = list(input().strip() for _ in range(c)) # wrong
stack = [int(input()) for _ in range(c)]
# 입력받은 막대기의 높이를 리스트에 저장하는 부분에서 strip() 함수를 사용하였습니다. 하지만 이 경우에는 리스트에 저장된 각각의 문자열의 양쪽 공백을 제거하는 것이 아니라, 문자열의 맨 앞과 맨 뒤의 공백만 제거하게 됩니다. 이러한 경우에는 입력값이 예상과 다르게 처리될 가능성이 있으므로 strip() 함수를 사용하지 않는 것이 좋습니다.

# print - 공백 간격두고 한 줄로 프린트
print(" ".join(map(str, stack)))