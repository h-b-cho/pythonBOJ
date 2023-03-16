# from collections import deque

# https://jungeun960.tistory.com/148
# https://dilee.tistory.com/19?category=961425

class Stack:
    def __init__(self, size = 5):
        self.stack = [] #stack 리스트 생성
        self.size = size #stack 의사이즈
        self.top = 0 #SP(Stack Pointer) stack에 저장되는 데이터의 개수

    def push(self,data):
        if data in self.stack:
            print("{} 값은 중복된 데이터입니다.".format(data))
        else:
            if self.size > self.top:
                self.stack.append(data)
                self.top += 1
                print("{} 값을 스택에 추가합니다.".format(data))
            else:
                print("overflow 발생...스택이 가득찼습니다.")
        self.view()

    def pop(self):
        if self.top <= 0:
            print("underflow 발생...스택에 값이 존재하지 않습니다.")
        else:
            print("{} 값을 pop() 했습니다.".format(self.stack[-1]))
            del self.stack[-1]
            self.top -= 1
        self.view()

    def view(self):
        print("스택에 저장된 데이터", end = "")
        if self.top <= 0:
            print("가 존재하지 않음...underflow")
        else:
            print(": ", end = "")
            for elem in self.stack:
                print(elem, end = " ")
            print()

class Queue:
    def __init__(self, size = 5):
        self.queue = [] #큐를 리스트로 구현
        self.size = size #큐의 사이즈
        self.front = 0 #큐의 앞쪽 포인터
        self.rear = 0 #큐의 뒤쪽 포인터

    def enqueue(self, data):
        if data in self.queue: #중복된 값 방지
            print("{} 값은 이미 큐에 있는 데이터입니다.".format(data))
        else:
            if self.size <= self.rear: #큐의 사이즈가 rear 보다 작으면 overflow 
                print("overflow...큐가 가득찼습니다.")
            else: 
                self.queue.append(data)
                self.rear += 1 #추가했을 때, rear 크기 증가
                print("{} 값을 추가했습니다.".format(data))
            self.view()

    def dequeue(self):
        if self.size <= 0 or self.rear == self.front:
            print("dequeue() 를 실행할 값이 없습니다.")
        else:
            print("{} 값을 추출했습니다.".format(self.queue[0]))
            del self.queue[0]
            self.front += 1 #추출했을 때, front 값 증가
        self.view()

    def view(self):
        print("큐의 데이터 값: ", end ='')
        if self.size <= 0 or self.rear == self.front:
            print("없음")
        else:
            for elem in self.queue:
                print(elem, end = " ")
            print()


# 큐(Queue)

# 가장 먼저 넣은 데이터를 가장 먼저 꺼낼 수 있는 구조(FIFO) -> 오른쪽에 입력 왼쪽으로 출력
# deque를 사용해 append(), popleft() 사용
# 데이터를 입력된 순서대로 처리해야 할 때, BFS(너비 우선 탐색) 구현 할 때 사용


# 디큐 함수 ( from collections import deque)

# 스택 구현(오른쪽 끝에서 입출력) : append(), pop()
# 큐 구현 : appendleft(), pop(), append(), popleft()
# depue 확장하기 : extend(), extendleft()
# 리스트 처럼 수정 삭제 : insert(), remove()
# deque 내용 좌우로 반전 : reverse()
# 회전 : rotate(n)
# 모든 원소 제거 : clear()