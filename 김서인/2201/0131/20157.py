import sys
import collections

input = sys.stdin.readline

slope = collections.defaultdict(int)

N = int(input())
balloons = list(tuple(map(int, input().split())) for _ in range(N))

def find_gcd(a,b): # 유클리드 호제법

    while b != 0:
        r = a % b
        a,b = b, r

    return abs(a)

# 기울기 구하기
for x, y in balloons:
    if x == 0 and y == 0:  # 0, 0에는 풍선 둘 수 없음
        continue
    elif x == 0:  # x축만 0이면
        # 방향 두개로 나뉨
        if y < 0:
            slope[(0, -1)] += 1
        else:
            slope[(0, 1)] += 1

    elif y == 0:  # y축만 0이면
        # 방향 두 개로 나뉨
        if x < 0:
            slope[(-1, 0)] += 1
        else:
            slope[(1, 0)] += 1

    else:
        gcd = find_gcd(x, y)
        x //= gcd
        y //= gcd
        slope[(x, y)] += 1

# 젤 풍선 많이 터뜨릴 수 있는 방향일 때, 그 점수 구하기
ans = 0
for value in slope.values():
    ans = max(ans, value)

print(ans)
