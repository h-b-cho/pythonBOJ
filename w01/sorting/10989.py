# 같은 문제: 2750번, 2751번 | 메모리제한이 256mb에서 8mb
# arr내의 수는 10,000보다 작거나 같은 자연수이다.
import sys
input = sys.stdin.readline

# 답 01 [메모리초과] ------------------------------------------
N = int(input())
arr = []
for _ in range(N):
  arr.append(int(input()))

for i in sorted(arr):
  print(i)

# 답 02 [메모리초과] ------------------------------------------
arr = [0]*10000
N = int(input())
inpList = []
for _ in range(N):
    inpList.append(int(input()))

for inp in inpList:
    arr[inp-1]+=1  # 예를 들어 arr[4]의 값이 2일 때, inp==5가 2회 중복입력 됨

i = 0

for arritem in arr:
    i+=1
    if arritem!=0:
        for _ in range(arritem):
	        print(i)
     
# 답 03 ------------------------------------------
arr = [0]*10000
n = int(input())
for _ in range(n):
  inpval = int(input())
  arr[inpval-1]+=1

for i in range(0, 10000):
  # i == inpval-1
  if arr[i]!=0:
    for _ in range(arr[i]):
      print(i+1) # i+1 == inpval

# https://velog.io/@hbtopkr/%EC%88%98-%EC%A0%95%EB%A0%AC%ED%95%98%EA%B8%B0-3-%EB%A9%94%EB%AA%A8%EB%A6%AC%EC%A0%9C%ED%95%9C-sorted-%EB%8C%80%EC%8B%A0-%EB%B0%B0%EC%97%B4%EC%9D%98-%EC%9D%B8%EB%8D%B1%EC%8A%A4-%EA%B0%92-%EC%9D%B4%EC%9A%A9