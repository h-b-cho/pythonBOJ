import sys
input = sys.stdin.readline
N = int(input())

stairs = list()
for _ in range(N):
    stairs.append( int(input()) )

dp = [0]*N  # dp[i]에 i번째 계단까지 올라왔을 때 얻을 수 있는 최대 점수를 저장.

if N<=2:
    print(sum(stairs))
elif N==3:
    print(max( stairs[0]+stairs[2], stairs[1]+stairs[2]) )
else:
    dp[0] = stairs[0]
    dp[1] = stairs[0]+stairs[1]
    dp[2] = max( stairs[0]+stairs[2] , stairs[1]+stairs[2] )
    for i in range(3, N):
        dp[i] = max( dp[i-2]+stairs[i] , dp[i-3]+stairs[i-1]+stairs[i] )
    print(dp[-1])