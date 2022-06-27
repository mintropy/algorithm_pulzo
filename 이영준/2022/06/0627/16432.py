"""
Title : 떡장수와 호랑이
Link : https://www.acmicpc.net/problem/16432
"""

from sys import stdin

input = stdin.readline
MIIS = lambda: map(int, input().split())

if __name__ == "__main__":
    N = int(input())
    dduks = [tuple(map(int, input().split())) for _ in range(N)]
    if N == 1:
        print(dduks[0][1])
        exit()

    dp = [[-1] * 10 for _ in range(N)]
    last_day = dduks[0][1:]
    for i in range(1, N):
        today = []
        for x in dduks[i][1:]:
            for y in last_day:
                if x != y:
                    dp[i][x] = y
                    today.append(x)
                    break
        last_day = today[::]

    ans = []
    for x in range(10):
        if dp[-1][x] == -1:
            continue
        ans.append(x)
        idx = N - 1
        while N:
            ans.append(dp[idx][ans[-1]])
            idx -= 1
            if dp[idx][ans[-1]] == -1:
                break
        break
    if len(ans) == N:
        ans.reverse()
        print(*ans, sep="\n")
    else:
        print(-1)

"""
Counter Example

15
3 5 6 7
4 6 7 8 9
2 4 6
1 4
4 1 4 5 6
4 4 6 7 8
2 2 4
4 2 3 6 7
1 5
4 2 3 7 8
3 3 4 8
4 1 3 5 8
1 5
2 3 8
5 2 3 4 6 9

out
-1

ans
5
7
6
4
1
6
4
2
5
2
4
1
5
8
2

1
1 1

"""
