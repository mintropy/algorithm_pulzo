"""
Title : 소가 길을 건너간 이유 5
Link : https://www.acmicpc.net/problem/14465
"""

import sys
input = sys.stdin.readline
n, k, b = map(int, input().split())

traffic_light = sorted([int(input()) - 1 for _ in range(b)])
# tl_s부터 tl_e - 1 인덱스에 해당하는 신호등이 선택됨
# 두개가 같으면 고치는 신호등이 없음
tl_s, tl_e = 0, 0

# 해당 범위에서 고친 신호등 개수
traffic_light_fix = 0
# k 길이 범위 설정
st = 0
end = k - 1
# k 길이 범위에서 고치는 신호등 개수 확인
while True:
    if tl_s < b and  tl_e < b and traffic_light[tl_e] <= end:
        traffic_light_fix += 1
        tl_e += 1
    else:
        break

# 최솟값 설정
min_traffic_light_fix = traffic_light_fix

for _ in range(end, n - 1):
    st += 1
    end += 1
    if tl_s < b and traffic_light[tl_s] < st:
        tl_s += 1
        traffic_light_fix -= 1
    if tl_e < b and traffic_light[tl_e] == end:
        tl_e += 1
        traffic_light_fix += 1
    if traffic_light_fix < min_traffic_light_fix:
        min_traffic_light_fix = traffic_light_fix

print(min_traffic_light_fix)