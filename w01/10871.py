import sys
input = sys.stdin.readline

n, x = map(int, input().split())
nxlist = list(map(int, input().split()))

for i in nxlist:  # 따로 설정되진 않았으나 자동으로 리스트 nxlist의 len만큼 반복
    if(i < x):
        print(i)