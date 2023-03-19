def Tree():
    import sys
    input = sys.stdin.readline
    N = int(input())
    Fal = str(".")

    tree = dict()

    for _ in range(N):
        root, leftnd, rightnd = input().split()
        tree[root] = [leftnd, rightnd]

    def Preorder(root):
        if root!=Fal:
            print(root, end='')
            Preorder(tree[root][0])
            Preorder(tree[root][1])

    def Inorder(root):
        if root!=Fal:
            Inorder(tree[root][0])
            print(root, end='')
            Inorder(tree[root][1])

    def Postorder(root):
        if root!=Fal:
            Postorder(tree[root][0])
            Postorder(tree[root][1])
            print(root, end='')

    Preorder("A")
    print(end="\n")
    Inorder("A")
    print(end="\n")
    Postorder("A")
    print(end="\n")
Tree()