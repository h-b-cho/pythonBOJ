N = int(input())
graph = [[] for _ in range(N+1)]

for i in range(1, N+1):
    node,left,right = map(str, input().split())
    graph[i].append(node)
    graph[i].append(left)
    graph[i].append(right)

# graph = [
#     [],
#     ['A', 'B', 'C'],
#     ['B', 'D', '.'],
#     ['C', 'E', 'F'],
#     ['D', '.', '.'],
#     ['E', '.', '.'],
#     ['F', '.', 'G'],
#     ['G', '.', '.'],
# ]

def Preorder(node):
    print(graph[node][0], end='')
    if graph[node][1] != '.':
        for i in range(1, N+1):
            if graph[i][0] == graph[node][1]:
                Preorder(i)
    if graph[node][2] != '.':
        for i in range(1, N+1):
            if graph[i][0] == graph[node][2]:
                Preorder(i)

# def Inorder():
#     if graph[node][1] != '.':
#         for i in range(1, N+1):
#             if graph[i][0] == graph[node][1]:
#                 tree(i)
#     print(graph[node][0], end='')
#     if graph[node][2] != '.':
#         for i in range(1, N+1):
#             if graph[i][0] == graph[node][2]:
#                 tree(i)

# def Postorder():
#     if graph[node][2] != '.':
#         for i in range(1, N+1):
#             if graph[i][0] == graph[node][2]:
#                 tree(i)
#     if graph[node][1] != '.':
#         for i in range(1, N+1):
#             if graph[i][0] == graph[node][1]:
#                 tree(i)
#     print(graph[node][0], end='')

Preorder(node)
# Inorder()
# Postorder()