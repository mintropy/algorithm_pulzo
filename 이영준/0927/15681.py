"""
Title : 트리와 쿼리
Link : https://www.acmicpc.net/problem/15681
"""

import sys, collections
input = sys.stdin.readline

n, r, q = map(int, input().split())
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

# 각 점의 부모 찾기
parents = [0] * (n + 1)

# 부모 찾는 과정 순서로 담아, 자식수 확잉 용도로 사용
stack = [r]
visited = [False] * (n + 1)
visited[r] = True
queue = collections.deque([r])
while queue:
    v = queue.popleft()
    for w in tree[v]:
        if not visited[w]:
            stack.append(w)
            queue.append(w)
            visited[w] = True
            parents[w] = v

# 모든 점은 스스로 트리를 구성하고 1개가 됨
child_count = [1] * (n + 1)
# 부모 찾은 역과정 : stack 을 활용 부모에 자식들 정점 개수 더해주기
for _ in range(n - 1):
    v = stack.pop()
    child_count[parents[v]] += child_count[v]

for _ in range(q):
    print(child_count[int(input())])
