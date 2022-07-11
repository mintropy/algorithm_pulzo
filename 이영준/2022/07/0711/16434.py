"""
Title : 드래곤 앤 던전
Link : https://www.acmicpc.net/problem/16434
"""

from sys import stdin

input = stdin.readline
MIIS = lambda: map(int, input().split())


def bin_search(H: int, dungeons: list[tuple[int]]) -> int:
    left, right = 0, 10**17
    ans = 0
    while left <= right:
        mid = (left + right) // 2
        if simulate(mid, H, dungeons):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    return ans


def simulate(health: int, attack: int, dungeons: list[tuple[int]]) -> bool:
    max_health = health
    for t, a, h in dungeons:
        if t == 1:
            turn = h // attack if h % attack == 0 else h // attack + 1
            if health - a * (turn - 1) <= 0:
                break
            health -= a * (turn - 1)
        else:
            attack += a
            health = min(health + h, max_health)
    else:
        return True
    return False


# if __name__ == "__main__":
#     N, H = MIIS()
#     dungeons = [tuple(MIIS()) for _ in range(N)]
#     print(bin_search(H, dungeons))

"""
용사 능력치
    최대 생명력
    현재 생명력
    공격력

던전 N개방
    i > i + 1번방
방에 들어간 경우
    1. 공격력 만큼 몬스터 생명력 갂기
    2. 몬스터 생명력 0이하 -> 다음방
    3. 몬스터 공격력 만큼 용사 현재 생명력 갂기
    4. 용사 생명력 0 이하 -> 사망
    5. 1부터 다시
"""

# ---------------------------------------------

from sys import stdin

input = stdin.readline
MIIS = lambda: map(int, input().split())


if __name__ == "__main__":
    N, H = MIIS()
    HP = 0
    answer = 0
    for _ in range(N):
        t, a, h = MIIS()
        if t == 1:
            turn = h // H if h % H == 0 else h // H + 1
            HP += a * (turn - 1)
            answer = max(answer, HP)
        else:
            H += a
            HP = max(HP - h, 0)
    print(answer + 1)
