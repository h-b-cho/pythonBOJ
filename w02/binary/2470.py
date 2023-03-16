import sys
input = sys.stdin.readline
N = int(input())
litters = sorted(list(map(int, input().split())))

def binary_search(srtarr:list):
    min   = 0
    max   = N-1
    sum   = abs(srtarr[min]+srtarr[max])
    result = [srtarr[min], srtarr[max]]

    while min<max:
        srtarrMin = srtarr[min]
        srtarrMax = srtarr[max]

        tmpsum = abs(srtarrMin+srtarrMax)

        if tmpsum<sum:
            sum = tmpsum
            result = [srtarrMin, srtarrMax]
            if sum==0:
                break

        if tmpsum<0:
            min+=1
        else: 
            max-=1

    print(result[0], result[1])

binary_search(litters)