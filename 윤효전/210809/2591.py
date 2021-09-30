import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

S = input().rstrip()

dp = {}
def rec(s:str):
    if len(s) == 0:
        return 1
    if s in dp:
        return dp[s]

    a, b = 0, 0
    if 1 <= int(s[0]):
        a = rec(s[1:])
        if len(s) >= 2 and 34 >= int(s[:2]):
            b = rec(s[2:])
        dp[s] = a + b
        return a + b
    else:
        return 0

print(rec(S))