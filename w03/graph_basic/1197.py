import sys
input = sys.stdin.readline
V, E = map(int, input().split()) 

edge = []
for _ in range(E):
    a, b, w = map(int, input().split())
    edge.append((w, a, b))    # 입력으로 주어진 V개의 정점과 S개의 간선을 edge 리스트에 저장. 각 원소는 (간선 가중치, 출발 정점, 도착 정점)의 형태.

edge.sort(key=lambda x: x[0]) # 가중치의 오름차순으로 정렬.

parent = list(range(V + 1))   # 각 정점의 부모가 자기 자신으로 초기화.

def union(a, b):
    a = find(a)
    b = find(b)

    if b < a:
        parent[a] = b
    else:
        parent[b] = a

def find(a):                    # 경로 압축(Path Compression) 기법을 사용하여, 재귀적으로 부모를 찾아올 때 중간 경로의 모든 정점의 부모를 최상위 부모로 갱신해주고 있다.
    if a == parent[a]:
        return a
    parent[a] = find(parent[a]) # 경로 압축
    return parent[a]

sum = 0
for w, s, e in edge:
    if find(s) != find(e): # edge 리스트를 가중치의 오름차순으로 순회하면서 각각의 간선을 선택하면서 최소 비용 신장 트리를 구성합니다. 이때, 선택한 간선의 두 정점이 이미 같은 집합에 속해 있으면 사이클을 형성하므로 해당 간선은 선택하지 않고 다음으로 작은 가중치의 간선을 선택합니다.
        union(s, e)
        sum += w           # 선택한 간선들의 가중치 합을 출력. 

print(sum)