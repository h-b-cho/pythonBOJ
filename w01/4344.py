import sys
input = sys.stdin.readline

c = int(input())

for i in range(c):
  arr = list(map(int, input().split()))
  scores = arr[1:]
  avrge = sum(scores)/arr[0] 

  p = 0
  for j in range(len(scores)):
    if scores[j]>avrge:
      p += 1
  
  print(f'{p/arr[0]*100:.3f}%') # 답
  # print('{0:.3f}%'.format(p/arr[0]*100)) # 답
  
  # print('%0.3f' % (p/arr[0]*100)) # 퍼센테이지 숫자만

  # print(str(round(p/arr[0], 5)*100)+'%') # 오답