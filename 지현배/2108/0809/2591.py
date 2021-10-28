cards = list(map(int, list(input().rstrip())))
length = len(cards) - 1
dp = [0 for _ in range(length + 1)] +[1]
if cards[length] != 0:
    dp[length] = 1
for idx in range(length - 1, -1, -1):
    target = cards[idx]
    if target == 0:
        continue
    dp[idx] += dp[idx + 1]
    if 0 < cards[idx] * 10 + cards[idx + 1] < 35:
        dp[idx] += dp[idx + 2]
print(dp[0])