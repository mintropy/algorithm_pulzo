"""
Title : 고층 건물
Link : https://www.acmicpc.net/problem/1027
"""

# 기울기를 나누어서 구하는 것 보다, 곱하는 방식으로 계산하자
# 나누어서 계산하면 부동소수점 문제로, 정확한 값을 찾기 힘들다

import sys
input = sys.stdin.readline

N = int(input())
buildings = list(map(int ,input().split()))

max_count = 0

for i in range(N):
    height = buildings[i]
    # 바로 왼쪽 / 오른쪽에 건물이 있다면 무조건 가능
    count = 2
    if i == 0:
        count -= 1
    if i == N - 1:
        count -= 1
    # 왼쪽으로 확인
    last_left = i - 1
    left_idx = i - 2
    while left_idx >= 0:
        # 탐색 인덱스 조정
        # 이전 건물과 비교해서 가능한지
        # 기울기 음수 >> 양수 or 음수라면 기울기 증가 or 양수라면 기울기 감소
        if (height >= buildings[last_left] and height < buildings[left_idx]) or\
            (height > buildings[last_left] and height <= buildings[left_idx]) or\
            (height > buildings[last_left] and height > buildings[left_idx] and\
            (height - buildings[last_left]) * (i - left_idx) > (height - buildings[left_idx]) * (i - last_left)) or\
            (height < buildings[last_left] and height < buildings[left_idx] and\
            (height - buildings[last_left]) * (i - left_idx) > (height - buildings[left_idx]) * (i - last_left)):
                count += 1
                last_left = left_idx
        left_idx -= 1
    # 오른쪽으로 확인
    last_right = i + 1
    right_idx = i + 2
    while right_idx < N:
        # 탐색 인덱스 조정
        # 이전 건물과 비교해서 가능한지
        if (height > buildings[last_right] and height <= buildings[right_idx]) or\
            (height >= buildings[last_right] and height < buildings[right_idx]) or\
            (height > buildings[last_right] and height > buildings[right_idx] and\
            (height - buildings[last_right]) * (i - right_idx) < (height - buildings[right_idx]) * (i - last_right)) or\
            (height < buildings[last_right] and height < buildings[right_idx] and\
            (height - buildings[last_right]) * (i - right_idx) < (height - buildings[right_idx]) * (i - last_right)):
                count += 1
                last_right = right_idx
        right_idx += 1
    if max_count < count:
        max_count = count

print(max_count)
