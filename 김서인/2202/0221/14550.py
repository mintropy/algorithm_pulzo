import sys

input = sys.stdin.readline

while True:
    try:
        N, S, T = map(int, input().split())
        board = []
        cnt = 0
        while cnt < N:
            tmp = list(map(int, input().split()))
            cnt += len(tmp)
            board.extend(tmp)

        dp = [[False] * (N) for _ in range(T)]
        # 초기값
        for i in range(S):
            dp[0][i] = board[i]

        for i in range(1, T - 1):
            for j in range(N):
                tmp = -987654321
                if j == 0:
                    tmp = 0
                for k in range(1, S + 1):
                    if N > j - k >= 0:
                        if dp[i - 1][j - k] == False:
                            pass

                        else:
                            tmp = max(tmp, dp[i - 1][j - k])

                dp[i][j] = tmp + board[j]

        # 마지막
        for j in range(N):
            tmp = 0
            for k in range(1, S + 1):

                if j - k < 0:
                    pass
                else:
                    tmp = max(tmp, dp[-2][j - k])

            dp[-1][j] = tmp + board[j]

        ans = -9987654321
        for i in range(1, S + 1):
            ans = max(ans, dp[-2][-i])
        print(ans)

    except:
        break
