import sys
from collections import defaultdict

input = sys.stdin.readline

D, N = map(int, input().split())
max_hot_temperatures = [int(input()) for _ in range(D)]
clothes_fancy = {}
clothes_fancy_reverse = {}
clothes_fancy_scores = []
for i in range(N):
    low, high, score = map(int, input().split())
    clothes_fancy[score] = i
    clothes_fancy_reverse[i] = score
    clothes_fancy_scores.append((low, high, score))

dp = [[0] * N for _ in range(D)]

# 날짜 별로 입을 수 있는 옷들 저장(화려함 기준으로)
can_wear = defaultdict(list)
for i in range(D):
    temperature = max_hot_temperatures[i]
    for j in range(N):
        low, high, fancy_score = clothes_fancy_scores[j]
        if low <= temperature <= high:
            can_wear[i].append(fancy_score)

# 날짜 쭉~
for i in range(1, D):
    for j in can_wear[i]:  # 그날 입을 수 있는 옷들
        idx = clothes_fancy[j]
        for k in can_wear[i - 1]:  # 전날 입을 수 있는 옷들
            cloth_idx = clothes_fancy[k]
            dp[i][idx] = max(dp[i][idx], dp[i - 1][cloth_idx] + abs(j - k))

# 정답 출력
print(max(dp[-1]))
