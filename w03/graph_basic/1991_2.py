def Tree():
    import sys
    input = sys.stdin.readline
    N = int(input())
    
    # TREE = ["A", ["B", ["D", [], [] ], [] ], ["C", ["E", [], [] ], ["F", [], ["G", [], [] ] ] ] ]
    
    TREE = ["A", 
                ["B", 
                    ["D", 
                        [], 
                        []
                    ], 
                    []
                 ], 
                ["C",
                    ["E", 
                        [], 
                        []
                     ], 
                    ["F",
                        [], 
                        ["G", 
                            [], 
                            []
                         ]
                     ]
                 ]
            ]

    def Inorder(tree):
        if tree:
            Inorder(tree[1]) 
            print(tree[0], end='')
            Inorder(tree[2])

    def Preorder(tree):
        if tree:
            print(tree[0], end='')
            Preorder(tree[1])
            Preorder(tree[2])

    def Postorder(tree):
        if tree:
            Postorder(tree[1])
            Postorder(tree[2])
            print(tree[0], end='')

    Preorder(TREE)
    print(end="\n")
    Inorder(TREE)
    print(end="\n")
    Postorder(TREE)
    print(end="\n")
Tree()