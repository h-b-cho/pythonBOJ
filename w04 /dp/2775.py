T = int(input())

for _ in range(T):
    A = int(input())  # 층 k
    B = int(input())  # 호 n

    floor_0 = [ i for i in range(1, B+1) ]
    for a in range(0, A):       # 0 ~ a-1층 까지를 for문 돌려서 a층에 대한 값 얻는 것
        for b in range(1, B): # 1 ~ b-1호 까지를 for문 돌려서 b호에 대한 값 얻는 것
            floor_0[b] += floor_0[b-1]
    print(floor_0[-1])