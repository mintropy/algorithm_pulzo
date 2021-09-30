import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

N = int(input())
S = [0] + [list(map(int, input().split())) for _ in range(N-1)]
K = int(input())


def dfs(now, ac, rageArt):
    if now == N:
        return ac
    elif now > N:
        return float('inf')
    else:
        ret = []
        ret.append(dfs(now+1, ac+S[now][0], rageArt))
        ret.append(dfs(now+2, ac+S[now][1], rageArt))
        if rageArt:
            ret.append(dfs(now+3, ac+K, False))
        return min(ret)


print(dfs(1, 0, True))
