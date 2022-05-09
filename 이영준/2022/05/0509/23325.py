"""
Title : 마법천자문
Link : https://www.acmicpc.net/problem/23325
"""

import sys
input = sys.stdin.readline


if __name__ == "__main__":
    string = input().strip()
    l = len(string)
    string = f"+{string}   "
    calculations = {
        "+-": 1, "++": 10, "++-": 11,
        "--": -1, "-+": -10, "-+-": -11,
    }
    dp = [-1_000_000] * (l + 2)
    dp[0] = 0
    for i in range(l):
        before = dp[i]
        if before == -1_000_000:
            continue
        next1 = string[i:i+2]
        next2 = string[i:i+3]
        if next1 in calculations:
            next1 = calculations[next1]
            if dp[i+2] < before + next1:
                dp[i+2] = before + next1
        if next2 in calculations:
            next2 = calculations[next2]
            if dp[i+3] < before + next2:
                dp[i+3] = before + next2
    print(dp[-1])
