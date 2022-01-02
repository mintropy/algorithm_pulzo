'''
치킨 배달

'''
import sys
input = sys.stdin.readline
from itertools import combinations
N, M = map(int,input().split())

# 집과 치킨집 위치 저장
homes = []
chicken_list = []

# 입력을 받으면서 저장
for i in range(N):
    list_ = list(map(int,input().split()))
    for j in range(N):
        if list_[j] == 1:
            homes.append((i,j))
        elif list_[j] == 2:
            chicken_list.append((i,j))

# 조합을 통해서 치킨집 고르기
# M보다 작은 수의 치킨집은 생각할 필요 없음.
# 어차피 수가 적은 거 보다 많은게 거리를 줄일 수 있기 때문
C_chickens = list(combinations(chicken_list,M))
min_total = 987654321

# 각 조합의 치킨집 마다 거리를 구하기
for chickens in C_chickens:
    total = 0
    # 각 집에서 출발하여 가장 짧은 거리의 치킨집 찾기
    for home in homes:
        min_dis = 987654321
        # 각 치킨 집까지의 거리를 구하기
        for chicken in chickens:
            dis= abs(chicken[0] - home[0]) + abs(chicken[1] - home[1])
            # 각 집에서 치킨집까지 최소 거리 저장
            if min_dis > dis:
                min_dis = dis
        # 최소 거리를 총 거리에 저장
        total += min_dis
    # 최소 총 거리 저장
    if min_total > total:
        min_total = total

print(min_total)