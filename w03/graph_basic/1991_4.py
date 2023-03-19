import sys
N = int(sys.stdin.readline())
tree = [list(map(str, sys.stdin.readline().split())) for _ in range(N)]

# tree = [
#     ['A', 'B', 'C'],
#     ['B', 'D', '.'],
#     ['C', 'E', 'F'],
#     ['D', '.', '.'],
#     ['E', '.', '.'],
#     ['F', '.', 'G'],
#     ['G', '.', '.'],
# ]

Fal = str(".")

def preorder(i):
    root = tree[i][0]
    left = tree[i][1]
    right = tree[i][2]
    print(root, end="")
    if left!=Fal:
        preorder(ord(left) - 65)
    if right!=Fal:
        preorder(ord(right) - 65)

def inorder(i):
    root = tree[i][0]
    left = tree[i][1]
    right = tree[i][2]
    if left!=Fal:
        inorder(ord(left) - 65)
    print(root, end="")
    if right!=Fal:
        inorder(ord(right) - 65)
 
def postorder(i):
    root = tree[i][0]
    left = tree[i][1]
    right = tree[i][2]
    if left!=Fal:
        postorder(ord(left) - 65)
    if right!=Fal:
        postorder(ord(right) - 65)
    print(root, end="")
    
preorder(0)
print(end="\n")
inorder(0)
print(end="\n")
postorder(0)