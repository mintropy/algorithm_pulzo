import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
V = int(input())
tree = [[] for _  in range(V + 1)]
for _ in range(V):
    node, *data = input().split()
    node = int(node)
    data = list(map(int, data))
    for i in range(len(data) // 2):
        tree[node].append([data[2 * i], data[2 * i + 1]])
maxV = maxN = 0
def DFS(node, parent, distance):
    cnt = 0
    for n, d in tree[node]:
        if n != parent:
            cnt += 1
            DFS(n, node, distance + d)
    if cnt == 0:
        global maxV, maxN
        if distance > maxV:
            maxV = distance
            maxN = node
DFS(1, 0, 0)
maxV = 0
DFS(maxN, 0, 0)
print(maxV)