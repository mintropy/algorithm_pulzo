"""
Title : 사회망 서비스(SNS)
Link : https://www.acmicpc.net/problem/2533
"""

import sys
sys.setrecursionlimit(1_000_000)
input = sys.stdin.readline


def dfs(now, before):
    global N, tree, dp
    if len(tree[now]) == 1:
        dp[now][0] = 1
        return
    for x in tree[now]:
        if x == before:
            continue
        dfs(x, now)
    dp[now][0] = 1 + sum(min(dp[x]) for x in tree[now])
    dp[now][1] = sum(dp[x][0] for x in tree[now])


if __name__ == "__main__":
    N = int(input())
    tree = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        u, v = map(int, input().split())
        tree[u].append(v)
        tree[v].append(u)
    
    dp = [[0, 0] for _ in range(N + 1)]
    dfs(1, 0)
    print(min(dp[1]))

'''
10
1 2
1 3
2 4
3 5
3 6
4 7
4 8
5 9
5 10
ans 4

5
1 5
2 5
3 5
4 5
ans 1

'''
