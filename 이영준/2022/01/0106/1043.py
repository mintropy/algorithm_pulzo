"""
Title : 거짓말
Link : https://www.acmicpc.net/problem/1043
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


def find_parent(x: int, parents: list) -> int:
    while x != parents[x]:
        x = parents[x]
    return x


def union_parent(x: int, root: int, parents: list) -> list:
    while x != 0:
        y = parents[x]
        if x == root:
            break
        parents[x] = root
        x = y
    return parents


n, m = MIIS()
wise_guy_count, *wise_guy = MIIS()

count_lie_story = 0

# 이야기 아는 사람은 0으로
parents = list(range(n + 1))
for p in wise_guy:
    parents[p] = 0

group = []
for _ in range(m):
    party_people_count, *party_people = MIIS()
    if party_people_count == 0:
        group.append([])
        continue
    # 각 그룹 확인용 추가
    group.append(party_people)
    # 각 사람에게 거짓말을 해도 되는지 확인
    people_parent = [find_parent(x, parents) for x in party_people]
    min_parent = min(people_parent)
    for p in party_people:
        if p != min_parent:
            parents = union_parent(p, min_parent, parents)

# 거짓말 해도 되는 파티 수
liar_party = 0
for g in group:
    for p in g:
        if find_parent(p, parents) == 0:
            break
    else:
        liar_party += 1

print(liar_party)
