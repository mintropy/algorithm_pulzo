"""
Title : 몬스터를 처치하자!
Link : https://www.acmicpc.net/problem/20008
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


def dfs(dagame_sum: int, time_now: int, cool_time: list):
    global N, HP, skills, min_time
    if time_now >= min_time:
        return
    if dagame_sum >= HP:
        min_time = time_now
        return
    # 각 스킬 확인해보고 사용
    for i in range(N):
        # 다음 바라볼 시간 : i번 스킬 남은 쿨타임 + 1
        t, dmg = skills[i]
        cool_time_left = cool_time[i] + 1
        next_cool_time = cool_time[::]
        for j in range(N):
            next_cool_time[j] -= cool_time_left
            if next_cool_time[j] < 0:
                next_cool_time[j] = 0
        next_cool_time[i] = t - 1
        dfs(dagame_sum + dmg, time_now + cool_time_left, next_cool_time)


N, HP = MIIS()
skills = [tuple(MIIS()) for _ in range(N)]
min_time = 10 ** 6

dfs(0, 0, [0] * N)

print(min_time)
