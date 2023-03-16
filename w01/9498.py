import sys
read = sys.stdin.readline

# -------------------------

# x = int(read())

# if x<=100 and x>=90:
#   print("A")
# elif x<90 and x>=80:
#   print("B")
# elif x<80 and x>=70:
#   print("C")
# elif x<70 and x>=60:
#   print("D")
# else:
#   print("F")

# -----

# x, y, w, h = map(int, read().split())

# print(min(x, y, w-x, h-y))

# -----

n = int(read())

for i in range(1, 10):
    print(n, "*", i, "=", n*i)