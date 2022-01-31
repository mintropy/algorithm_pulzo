'''
화살을 쏘자!

'''
import sys
input = sys.stdin.readline
from collections import defaultdict

N = int(input())

# 사분면 나누기
# 빈 리스트를 없애기 위해서 0을 추가
# 그리고 1개는 무조건 있기 때문에 1로 추가
quadrant1 = defaultdict(int)
quadrant1[0] += 1
quadrant2 = defaultdict(int)
quadrant2[0] += 1
quadrant3 = defaultdict(int)
quadrant3[0] += 1
quadrant4 = defaultdict(int)
quadrant4[0] += 1
# 하나씩 사분면을 기준으로 나누고
# 기울기를 비교하면서 저장
for _ in range(N):
    x, y = map(int,input().split())
    # 1사분면
    if x > 0 and y >= 0:
        # x축에 있을 경우
        if y == 0:
            quadrant1['v'] += 1
        # 나머지
        else:
            quadrant1[y/x] += 1
    # 2사분면
    elif x <= 0 and y > 0:
        if x == 0:
            quadrant2['v'] += 1
        else:
            quadrant2[y/x] += 1
    # 3사분면
    elif x < 0 and y <= 0:
        if y == 0:
            quadrant3['v'] += 1
        else:
            quadrant3[y/x] += 1
    # 4사분면
    elif x >= 0 and y < 0:
        if x == 0:
            quadrant4['v'] += 1
        else:
            quadrant4[y/x] += 1
# 그 값중에 가장 큰 값
print(max(max(quadrant1.values()),max(quadrant2.values()),max(quadrant3.values()),max(quadrant4.values())))
