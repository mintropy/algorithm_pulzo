import sys
input = sys.stdin.readline
def sol():
    N = int(input())
    jmp = [list(map(int, input().split())) for _ in range(N - 1)]
    K = int(input())
    dp = [[0], [100000]] + [[100000 for _ in range(i)] for i in range(1, N + 1)]
    for i in range(3 if N > 3 else N - 1):
        dp[i + 1][0] = min(dp[i + 1][0], dp[i][0] + jmp[i][0])
        dp[i + 2][0] = min(dp[i + 2][0], dp[i][0] + jmp[i][1])
        dp[i + 3][i + 1] = dp[i][0] + K
    for i in range(3, N - 1):
        dp[i + 3][i + 1] = dp[i][0] + K
        for j in range(i - 1):
            dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + jmp[i][0])
            dp[i + 2][j] = min(dp[i + 2][j], dp[i][j] + jmp[i][1])
    return min(dp[N - 1])
print(sol())