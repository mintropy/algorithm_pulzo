"""
Title : 개구리 점프
Link : https://www.acmicpc.net/problem/17619
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


def find_parents(x: int, parents: list) -> int:
    while x != parents[x]:
        x = parents[x]
    return x


def union_parents(x_parent: int, y_parent: int, parents: list) -> list:
    if x_parent < y_parent:
        parents[y_parent] = x_parent
    else:
        parents[x_parent] = y_parent
    return parents


n, q = MIIS()

parents = list(range(n + 1))

logs = []
for i in range(1, n + 1):
    x1, x2, y = MIIS()
    logs.append((i, x1, x2, y))
logs.sort(key=lambda x: (x[1], x[2]))


# 지금까지 나무의 마지막 부분
log_last = logs[0][2]
# 해당하는 나무의 부모
log_parent = logs[0][0]
for idx, x1, x2, y in logs:
    # 이전 나무의 마지막 부분까지 이어진다면
    if x1 <= log_last:
        # union
        if idx < log_parent:
            parents[log_parent] = idx
            log_parent = idx
        else:
            parents[idx] = log_parent
        # 나무가 더 뒷부분까지 이어질 수 있다면
        if x2 > log_last:
            log_last = x2
    # 아니라면
    else:
        # 새로운 부분 설정
        log_last = x2
        log_parent = idx

for _ in range(q):
    i, j = MIIS()
    if find_parents(i, parents) == find_parents(j, parents):
        print(1)
    else:
        print(0)


'''
Counter Example
3 3
1 5 1
2 3 2
4 6 3
1 2
1 3
2 3
ans : 1 1 1 
'''
