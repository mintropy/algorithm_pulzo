"""
Title : BFS 스페셜 저지
Link : https://www.acmicpc.net/problem/16940
"""

import collections
import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


def verify_bfs(n: int, tree: list, answer: list) -> int:
    if answer[0] != 1:
        return 0
    answer = collections.deque(answer[1:])
    queue = collections.deque([1])
    while answer or queue:
        # queue만 비어있고 answer 더 탐색해야하는 경우
        if answer and not queue:
            return 0
        # answer가 비어있는 경우
        if not answer:
            return 1
        # 아니라면 한 점을 꺼내어 인접점 확인
        x = queue.popleft()
        # x가 1이면 주변 모든 인접점 확인
        if x == 1:
            while tree[x]:
                if answer and answer[0] in tree[x]:
                    y = answer.popleft()
                    tree[x].remove(y)
                    queue.append(y)
                else:
                    return 0
        else:
            while len(tree[x]) > 1:
                if answer and answer[0] in tree[x]:
                    y = answer.popleft()
                    tree[x].remove(y)
                    queue.append(y)
                else:
                    return 0
    return 1


n = int(input())
tree = [set() for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = MIIS()
    tree[a].add(b)
    tree[b].add(a)

answer = list(MIIS())

print(verify_bfs(n, tree, answer))
