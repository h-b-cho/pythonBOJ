# 시험 시간에 못 풀었음!!

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
T = int(input()) 

def solve(root, start, end):
    for i in range(start, end):
        if inorder_arr[i] == preorder_arr[root]:
            solve(root + 1, start, i)
            solve(root + i + 1 - start, i + 1, end)
            print(preorder_arr[root], end=" ")

result = []
for _ in range(T):
    n = int(input())
    preorder_arr = [ map(int, input().split()) ]
    inorder_arr = [ map(int, input().split()) ]
    solve(0, 0, n)
    print('')
