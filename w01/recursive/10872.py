import sys
input = sys.stdin.readline

# sum = 1
# for i in range(1, int(input())+1):
#     sum = sum*(i)
# print(sum)

def factorial(n)->int:
    if(n==0):
        return 1
    else:
        return n*factorial(n-1)
#                n*
#                  n-1*
#                      (n-1)-1
#                             .
#                             .
#         if n==5
#         factorial(5) == 5*factorial(4)
#         factorial(4) == 4*factorial(3)
#         factorial(3) == 3*factorial(2)
#         factorial(2) == 2*factorial(1)
#         factorial(1) == 1*factorial(0)

print(factorial(int(input())))