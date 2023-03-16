
import sys
from itertools import combinations

while True:
    
    input_list = list(map(int, sys.stdin.readline().split()))

    k = input_list[0]
    num_list = input_list[1:]

    # print(k)

    if k==0:
        break

    c_result = list(combinations(num_list, 6))
    c_result.sort()
    
    for c in c_result:    # c: (1,2,3,4,5,6)
        
        c = list(c)       # c : [1,2,3,4,5,6]

        for i in c:
            
            print(i, end=' ')
        print()
        
    print()