import sys
input = sys.stdin.readline
N, C = input().split()
N = int(N)
C = int(C)
places = sorted(list(int(input()) for _ in range(N)))
placerange = places[1:]

# print( (min(places)+max(places))//C ) # wrong. 집의 좌표들이 1,2,3,...9인 경우에만 가능한 얘기.

result = 0

def binary_search(min, max):
    global result
    while min <= max:
        mid = (min+max) // 2
        cnt = 1
        cur = places[0]
        for i in placerange:
            if i - cur >= mid:
                cnt += 1
                cur = i
        if cnt >= C:
            min = mid + 1
            result = mid
        else:
            max = mid - 1
    return result

print(binary_search(1, places[-1]-places[0])) # == (1, max(places)-min(places))


# def binary_search(arr, start, end):
#     global result
#     if N == 2:
#         print(places[N-1]-places[0])  # == max(places)-min(places)
#     else:
#         while end >= start:
#             count = 0
#             # 1 2 4 8 9 places의 중앙값인 4가 mid가 되는 것이 아니라, 집들 사이의 최소 거리와 최대 거리의 중앙인 (1+8)/2 = 4(몫만 이용)가 되는 것이다.
#             mid = (start+end)//2
#             i = places[0]

#             for place in placerange:
#                 if place - i >= mid:
#                     count += 1
#                     i = place

#             if count >= C:
#                 result = mid
#                 start = mid+1
#             else:
#                 end = mid-1

#     return (result)


# print(binary_search(places, placerange[0], placerange[-1]))
