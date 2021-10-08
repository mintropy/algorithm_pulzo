import copy
import itertools
import sys


def set_cook_time(compliment):  # 칭찬 받아서 요리사의 음식 조리 시간 줄이기
    tmp = copy.copy(arr)
    for c in compliment:
        if tmp[c] == 1:
            continue
        tmp[c] -= 1
    return tmp


def calc_time(time):  # 그 시간이 주어지면, 요리 몇 개나 할 수 있는지
    res = 0
    for c in cook_time:
        res += (time // c)
    return res


def binary_search(left, right):
    tmp = 0
    while left <= right:
        mid = (left + right) // 2
        if calc_time(mid) >= K:  # 그 시간으로 요리 K개 이상할 수 있으면
            right = mid - 1
            tmp = mid
        else:
            left = mid + 1
    return tmp


input = sys.stdin.readline

N, K, C = map(int, input().split())

arr = list(map(int, input().split()))
min_cook_time = 10 ** 6 * K + 1

# 누구한테 격려해줄지
compliments = list(itertools.combinations_with_replacement(list(range(N)), C))

# 가능한 방법으로 모두 음식 조리 시간 셋팅 시도하기
for compliment in compliments:
    cook_time = set_cook_time(compliment)

    # 음식 조리 완료하는 최소 시간을 계산
    min_cook_time = min(min_cook_time, binary_search(0, K * max(arr)))

print(min_cook_time)
