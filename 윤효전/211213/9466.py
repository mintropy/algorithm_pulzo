import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def dfs(board, visit, root, i, n):
    if visit[i] != None:
        if visit[i][1] == root:
            return visit[i][0]
        else:
            return n
    visit[i] = (n, root)
    return dfs(board, visit, root, board[i], n+1)

T = int(input())
for _ in range(T):
    N = int(input()) # 2 <= N <= 100,000
    S = [None] + list(map(int, input().split()))
    visit = [None] * (N+1)
    ans = 0
    for i in range(1, N+1):
        if visit[i] == None:
            ans += dfs(S, visit, i, i, 0)
    print(ans)
    