N, r, c = map(int, input().split())
cnt = 0

while N != 0:
    N -= 1
    quarter = 2**N
    
    # 1사분면
    if r < quarter and c < quarter:
        cnt += quarter*quarter*0  #==pass

    # 2사분면
    elif r < quarter and c >= quarter:
        cnt += quarter*quarter*1
        c -= (quarter)

    # 3사분면
    elif r >= quarter and c < quarter:
        cnt += quarter*quarter*2
        r -= (quarter)

    # 4사분면
    else:
        cnt += quarter*quarter*3
        r -= (quarter)
        c -= (quarter)
print(cnt)