"""
Title : 완전 범죄
Link : https://www.acmicpc.net/problem/13700
"""

import sys, collections
input = sys.stdin.readline

n, s, d, f, b, k = map(int, input().split())
police = list(map(int, input().split()))

game_field = [False] * (n + 1)
# 경찰서는 들어가지 못하므로, 애초에 방문처리하여 가지 않게 함
for p in police:
    game_field[p] = True

# 위치, 버튼 누르는 횟수
queue = collections.deque([(s, 0)])
min_button = n + 1
while queue:
    pos, button = queue.popleft()
    # 종료 조건
    if button > min_button:
        break
    # 집에 도착
    if pos == d:
        if button < min_button:
            min_button = button
        continue
    # 앞, 뒤로 탐색
    if pos + f <= n and not game_field[pos + f]:
        game_field[pos + f] = True
        queue.append((pos + f, button + 1))
    if pos - b >= 1 and not game_field[pos - b]:
        game_field[pos - b] = True
        queue.append((pos - b, button + 1))

if min_button == n + 1:
    print('BUG FOUND')
else:
    print(min_button)
