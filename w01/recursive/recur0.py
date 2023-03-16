N = int(input())

def recurA(n):
  if n == 0:
    return
  recurA(n - 1)
  print(n)
  
# recurA(N) # 1\n2\n3

# 만약 위와 같이 코드가 짜여 있다면 과연 print(n)은 언제 실행되는 것일까?
# 만약 n==3이라서 recur(3) -> recur(2) -> recur(1) -> recur(0) 까지 가서 return을 만나 recur(0)이 종료, 다시 recur(1)로 돌아갔을 때, 
# recur(0)을 호출했던 recur(1) 밑에 print(n)이 있기에 그제야 n을 출력한다.
# 정답: 여기서 n은 1이다. 왜냐면 recur(1)이니까.
# 그래서 recur(1)도 이로써 종료, recur(2) 역시 여기서 연달아 print(n==2)를 수행하며 종료, recur(3)도 print(n==3)를 수행하며 종료하여 최종적으로 함수 실행이 끝난다.

# 참고로 print(n) 밑에는 return이 생략되어 있다. c로 예를 들자면 main문 쓸 때 마지막에 return 0 명시적으로 쓰지만 안 써도 문제는 없다. 파이썬도 동일하다. 

# 여하튼 함수의 끝을 만났기에 자기를 호출한 함수로 돌아가서 종료하고, 종료하고, 종료해서 더 이상 실행 중인 재귀가 없을 때 재귀는 종료된다.

def recurB(n):
    if n == 0:
        return print(n)
    recurB(n - 1)

# recurB(N) # 0
 
# 문제를 바꿔서 recur(3)을 실행하자. 최종 리턴 값은 0.

# 다시 문제를 바꿔보도록 하자. 우리가 만약 recur(0)의 값인 0을 최종적으로 리턴해야 한다면 어떻게 해야 할까? 

def recurC(n):
    if n == 0:
        return print(n)
    return recurC(n - 1)

recurC(N) # 0# 0 == recur(0)의 값
 
# 답은 간단하다. 호출된 재귀가 리턴한 값을 그대로 리턴하면 되는 것이다.


# https://veggie-garden.tistory.com/44