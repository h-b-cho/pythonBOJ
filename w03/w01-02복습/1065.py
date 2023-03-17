import sys
input = sys.stdin.readline
N = int(input())
cnt = 99

def isHan(x):
    global cnt
    if x<100:
        return x
    elif 100<=x<1000:
        for i in range(101, x+1):
            number = []             # number = list(map(int, str(x))) 로 처리하면 돼!~
            number.append(i//100)
            number.append((i//10)%10)
            number.append(i%10)
            if (number[0]-number[1]) == (number[1]-number[2]):
                cnt+=1
    else:
            # 네자리수 버전
            # number = []
            # number.append(i//1000)
            # number.append((i//100)%10)
            # number.append((i//10)%10)
            # number.append(i%10)
        return int(144)
    return cnt
        
print( isHan(N) )