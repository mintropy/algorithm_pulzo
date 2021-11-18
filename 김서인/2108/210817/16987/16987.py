import sys

input = sys.stdin.readline

n = int(input())
eggs = list(list(map(int, input().split())) for _ in range(n))  # 내구도, 무게
broken_eggs = []


def dfs(idx, cnt):  # cnt: 지금까지 몇 개 깼는지
    if idx == n:  # 가장 최근에 든 계란이 가장 오른쪽 계란이면 종료
        broken_eggs.append(cnt)
        return

    if eggs[idx][0] <= 0:  # 손에 든 계란이 깨졌으면
        dfs(idx + 1, cnt)
    else:

        # 만약 idx 빼고 모든 계란이 깨졌으면..
        chk_cnt = 0  # idx 빼고 모든 계란이 깨졌는지
        for i in range(n):
            if eggs[i][0] <= 0:
                chk_cnt += 1
        if chk_cnt >= n - 1:
            broken_eggs.append(cnt)
            return

        else:
            for i in range(n):
                broken_cnt = 0
                if i != idx and eggs[i][0] > 0:  # 깨지지 않은 계란 중에서 하나를 치는 거니까
                    # 손에 든 계란으로 다른 계란 부딪침 -> 서로 내구도 감소
                    eggs[idx][0] -= eggs[i][1]
                    eggs[i][0] -= eggs[idx][1]

                    if eggs[i][0] <= 0:  # 부딪친 후에 부딪침을 당한 계란이 깨졌으면
                        broken_cnt += 1

                    if (eggs[idx][0] + eggs[i][1] > 0) and eggs[idx][0] <= 0:  # 부딪친 후에 들고 있던 계란이 깨졌으면
                        broken_cnt += 1

                    dfs(idx + 1, cnt + broken_cnt)
                    eggs[idx][0] += eggs[i][1]
                    eggs[i][0] += eggs[idx][1]


dfs(0, 0)
print(max(broken_eggs))

"""
안 치는 경우를 언제나 고려하지 말고!
칠 수 없을 때만 안 쳐야 한다!!

in:
8
7 100
6 100
100 1
100 1
100 1
100 1
100 1
100 1

out:
6

"""
