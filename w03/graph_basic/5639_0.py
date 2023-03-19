###시간초과
###시간초과
###시간초과
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

tree={} 

while True:
    try:
        num=int(input())
        if len(tree)==0:
            root=num
            tree[root]=['*','*']
        else:
            curr=root
            while True:
                #왼쪽 서브 트리일 때
                if num<curr:
                    #왼쪽 노드가 없을 때
                    if tree[curr][0]=='*':
                        tree[curr][0]=num
                        tree[num]=['*','*']
                        break
                    #왼쪽 자식 노드로 이동
                    else:
                        curr=tree[curr][0]
                #오른쪽 서브 트리일 때
                else:
                    #오른쪽 노드가 없을 때
                    if tree[curr][1]=='*':
                        tree[curr][1]=num
                        tree[num]=['*','*']
                        break
                    #오른쪽 자식 노드로 이동
                    else:
                        curr=tree[curr][1]
    except:
        break

def postorder(curr):
    #왼쪽 자식 노드로 이동
    if tree[curr][0]!='*':
        postorder(tree[curr][0])
    #오른쪽 자식 노드로 이동
    if tree[curr][1]!='*':
        postorder(tree[curr][1])
    #현재 노드 출력
    print(curr)

postorder(root)