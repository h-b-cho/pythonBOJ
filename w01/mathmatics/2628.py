W, H = list(map(int, input().split()))
Row = [0, W]
Column = [0, H]
N = int(input())
for _ in range(N):
  a, b = map(int, input().split())
  if a==0:
    Column.append(b)
  else:
    Row.append(b)

Row.sort()
Column.sort()

num = 0
lst = []

def maxfinder(row, column):
  for i in range(0, len(row)-1):
    for j in range(0, len(column)-1):
      num = (row[i+1]-row[i]) * (column[j+1]-column[j])
      lst.append(num)
  return(max(lst))
  
print(maxfinder(Row, Column))