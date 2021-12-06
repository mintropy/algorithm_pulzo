"""
Title : 빌런 호석
Link : https://www.acmicpc.net/problem/22251
"""


def search(n: int, k: int, num: list, idx: int, p: int):
    # 가장 왼쪽 자리수부터 가능한 조합 넣으며 탐색
    # 모든 자리를 채웠으면, 최대 층수를 넘는지 확인
    global count, led_diff, floor_posibility
    if idx == k:
        if check_max_floor(n, num):
            count += 1
        return
    for floor, cost in floor_posibility[idx]:
        if cost <= p:
            num.append(floor)
            search(n, k, num, idx + 1, p - cost)
            num.pop()


def check_max_floor(n: int, num: list) -> bool:
    # int로 이루어진 num 리스트를 숫자로 바꾸어
    # 최대 층수를 넘으면 False
    floor = [str(i) for i in num]
    floor = int(''.join(floor))
    if floor > n or floor == 0:
        return False
    else:
        return True


# 최대 층수, 자리수, 최대 사용갯수, 지금 층
n, k, p, x = map(int, input().split())

# 위에서부터 아래로 각 자리별 LED 필요한지
led_need = {
    0: [1, 1, 1, 0, 1, 1, 1],
    1: [0, 0, 1, 0, 0, 1, 0],
    2: [1, 0, 1, 1, 1, 0, 1],
    3: [1, 0, 1, 1, 0, 1, 1],
    4: [0, 1, 1, 1, 0, 1, 0],
    5: [1, 1, 0, 1, 0, 1, 1],
    6: [1, 1, 0, 1, 1, 1, 1],
    7: [1, 0, 1, 0, 0, 1, 0],
    8: [1, 1, 1, 1, 1, 1, 1],
    9: [1, 1, 1, 1, 0, 1, 1],
}

# led 변경시 필요한 회수
led_diff = [[0] * 10 for _ in range(10)]
for i in range(10):
    for j in range(i):
        if i == j:
            continue
        for d in range(7):
            if led_need[i][d] != led_need[j][d]:
                led_diff[i][j] += 1
                led_diff[j][i] += 1

# 각 층의 현재 상태
floor_now = list(int(i) for i in str(x))
if len(floor_now) < k:
    floor_now = [0] * (k - len(floor_now)) + floor_now
# 각 자리별 가능한 숫자
floor_posibility = [[] for _ in range(k)]
for i in range(k):
    num_now = floor_now[i]
    for j in range(10):
        if j == num_now:
            floor_posibility[i].append((j, 0))
        elif led_diff[num_now][j] <= p:
            floor_posibility[i].append((j, led_diff[num_now][j]))


count = 0
search(n, k, [], 0, p)

# 원래 층을 합쳐서 탐색했으므로 -1
print(count - 1)


'''
counter example
15 2 4 5
ans: 8
output: 9
0층을 확인 안함
'''