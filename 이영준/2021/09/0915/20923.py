"""
Title :  숫자 할리갈리 게임
Link : https://www.acmicpc.net/problem/20923
"""

import sys, collections
input = sys.stdin.readline

n, m = map(int, input().split())

dodo = collections.deque([])
dodo_ground = collections.deque([])
suyeon = collections.deque([])
suyeon_ground = collections.deque([])

for _ in range(n):
    do, su = map(int, input().split())
    dodo.appendleft(do)
    suyeon.appendleft(su)

for i in range(m):
    # 수연의 차례
    if i % 2:
        suyeon_ground.append(suyeon.popleft())
        if not suyeon:
            print('do')
            break
    # 도도의 차례
    else:
        dodo_ground.append(dodo.popleft())
        if not dodo:
            print('su')
            break
    # 누군가 종을 칠 수 있는지
    # 수연이 종을 침
    if dodo_ground and suyeon_ground:
        if dodo_ground[-1] + suyeon_ground[-1] == 5:
            suyeon += dodo_ground + suyeon_ground
            suyeon_ground = collections.deque([])
            dodo_ground = collections.deque([])
    # 도도가 종을 침
    if (dodo_ground and dodo_ground[-1] == 5) or (suyeon_ground and suyeon_ground[-1] == 5):
        dodo += suyeon_ground + dodo_ground
        suyeon_ground = collections.deque([])
        dodo_ground = collections.deque([])
else:
    # 각자 덱에 카드가 없는 경우는 없음
    if len(dodo) > len(suyeon):
        print('do')
    elif len(dodo) < len(suyeon):
        print('su')
    else:
        print('dosu')
