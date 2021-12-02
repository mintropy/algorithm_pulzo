import copy
import sys

input = sys.stdin.readline

MIIS = lambda: map(int, input().split())

N, HP = MIIS()
skills = {}

for i in range(N):
    C, D = MIIS()
    skills[i] = (C, D)

ans = 10000000
ans_history = ''

def dfs(seconds: int, HP: int, skill_wait: list, history:str): # history는 디버깅용으로 만들었다.
    global ans, ans_history

    # 이미 정답 아니면
    if seconds >= ans:
        return

    # 몬스터 처치 했으면
    if HP <= 0:
        # 몬스터 처치하는 데 최소 시간
        ans = seconds
        ans_history = history
        return


    for i in range(N):
        new_skill_wait = copy.copy(skill_wait)
        tmp = new_skill_wait[i]
        if tmp < 0:
            tmp = 0
        # tmp+1초만큼 이동할 것
        tmp += 1

        for j in range(N):
            new_skill_wait[j] -= tmp
        # 스킬 사용하기
        new_skill_wait[i] = skills[i][0]-1

        dfs(seconds + tmp, HP - skills[i][1], new_skill_wait, history+f'{seconds}초: 스킬{i} |')


dfs(0, HP, [0] * N, '')
print(ans)
