"""
Title : 계란으로 계란치기
Link : https://www.acmicpc.net/problem/16987
"""


def search(n, eggs, egg_now, crashed):
    global max_crashed
    # 마지막 달걀까지 확인한 경우
    if egg_now == n:
        if crashed >= max_crashed:
            max_crashed = crashed
        return
    egg_stability, egg_weight = eggs[egg_now]
    # 깨진 달걀일 경우
    if egg_stability <= 0:
        search(n, eggs, egg_now + 1, crashed)
    else:
        egg_hit = False
        # 모든 달걀 확인
        for i in range(n):
            # 깨지지 않은 달걀이 있을 때
            if eggs[i][0] > 0 and i != egg_now:
                eggs[i][0] -= egg_weight
                eggs[egg_now][0] -= eggs[i][1]
                egg_hit = True
                crashed_plus = 0
                if eggs[egg_now][0] <= 0:
                    crashed_plus += 1
                if eggs[i][0] <= 0:
                    crashed_plus += 1
                search(n, eggs, egg_now + 1, crashed + crashed_plus)
                eggs[i][0] += egg_weight
                eggs[egg_now][0] += eggs[i][1]
        # 하나도 치지 않았을 경우
        if not egg_hit:
            search(n, eggs, egg_now + 1, crashed)


n = int(input())
eggs = [list(map(int, input().split())) for _ in range(n)]
max_crashed = 0

search(n, eggs, 0, 0)
print(max_crashed)
