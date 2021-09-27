import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, R, Q = map(int,input().split())
adj = list([] for _ in range(N+1))

for _ in range(N-1):
    a, b = map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)

def makeTree(currentNode, parent):
    for node in adj[currentNode]:
        if node != parent:
            child_list[currentNode].append(node)
            parent_list[node].append(currentNode)
            makeTree(node, currentNode)


def countSubtreenodes(currentNode):
    size[currentNode] = 1
    for node in child_list[currentNode]:
        countSubtreenodes(node)
        size[currentNode] += size[node]


parent_list = list([] for _ in range(N + 1))
child_list = list([] for _ in range(N + 1))

makeTree(R, -1)

size = list([0] for _ in range(N + 1))
countSubtreenodes(R)

for i in range(Q):
    q = int(input())
    print(size[q])