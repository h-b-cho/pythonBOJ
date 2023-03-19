import sys
sys.setrecursionlimit(10**6)
numarr = []
while True:
    try:
        num = int(input())
        numarr.append(num)
    except:
        break

def postorder(s, e):
    if s > e:
        return
    mid = e+1     # 루트보다 큰 값이 존재하지 않을 경우, 즉 오른쪽 자식이 없을 경우를 대비
    for i in range(s+1, e+1):
        if numarr[s] < numarr[i]:
            mid = i
            break
    postorder(s+1, mid-1)
    postorder(mid, e)
    print(numarr[s])

postorder(0, len(numarr)-1)