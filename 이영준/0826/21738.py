"""
Title : 얼음깨기 팽귄
Link : https://www.acmicpc.net/problem/21738
"""

import sys, collections
input = sys.stdin.readline


# 펭귄 위치를 루트로
n, s, p = map(int, input().split())
edges = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)

visited = [False] * (n + 1)
visited[p] = True

# 펭귄 위치를 루트로, 자식들만 우선 구하고 설정
# 각 자식별로 자식 번호를 키로
# 그 자식으로 따라가서, 가장 가까운 지지대 얼음까지 거리
# 자식에 있는 전체 얼음 개수를 값으로 저장
# penguin_child = {i: [0, 0] for i in edges[p]}
# 대신 가장 가까운 지지대 둘 까지 거리 저장
# 왼쪽에 작은값으로 저장
nearest_fixed_ice = [10 ** 6, 10 ** 6]

# 펭귄의 각 자식에서 시작 탐색
# 탐색하며 가장 가까운 지지대 얼음까지 거리 저장

for q in edges[p]:
    # ice_count = 0
    # fixed_ice = 0
    queue = collections.deque([(q, 1)])
    visited[q] = True
    # 얼음 설정
    # ice_count += 1
    if q <= s:
        # fixed_ice = 1
        d = 1
        if d < nearest_fixed_ice[1]:
            nearest_fixed_ice[1] = d
            if nearest_fixed_ice[1] < nearest_fixed_ice[0]:
                nearest_fixed_ice.reverse()
        continue
    while queue:
        x, d = queue.popleft()
        # if d >= nearest_fixed_ice[1]:
        #     break
        for y in edges[x]:
            # 방문했으면 넘어가기
            if visited[y]:
                continue
            # 지지대 얼음을 처음 만났을 때 종료
            # 값 저장 비교
            if y <= s:
                d += 1
                if d < nearest_fixed_ice[1]:
                    nearest_fixed_ice[1] = d
                    if nearest_fixed_ice[1] < nearest_fixed_ice[0]:
                        nearest_fixed_ice.reverse()
                break
            # ice_count += 1
            visited[y] = True
            queue.append((y, d + 1))
    # penguin_child[q] = [fixed_ice, ice_count]

print(n - sum(nearest_fixed_ice) - 1)


'''
# 연결된 얼음중, 지지대 얼음이 가장 가까운 두개 뽑기
# >> 지지대 얼음까지 거리가 0보다 큰 경우
ice = sorted(penguin_child.values(), key=lambda x:x[0])

# 1. 펭귄을 루트로 자식이 2인경우
# 2. 자식이 3개 이상인 경우
if len(ice) == 2:
    ice_break = (ice[0][1] - ice[0][0]) + (ice[1][1] - ice[1][0])
else:
    # 자식중 지지대가 없는 경우 먼저 더하기
    ice_break = 0
    for i in range(len(ice)):
        if ice[i][0]:
            break
        ice_break += ice[i][1]
    # 지지대까지 가장 거리 짧은 2개는 지지대까지 개수 제외 더하기
    for j in range(i, i + 2):
        ice_break += ice[j][1] - ice[j][0]
    # 나머지는 모든 얼음 개수 더하기
    for k in range(i + 2, len(ice)):
        ice_break += ice[k][1]

print(ice_break)
'''