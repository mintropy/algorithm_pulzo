import sys
from pprint import pprint
sys.stdin = open('input.txt')
input = sys.stdin.readline


def dfs(l, visit, n, ac):
    if visit[n]:
        return n
    visit[n] = 1
    ac.append(n)
    return dfs(l, visit, l[n], ac)


N = int(input())
S = [None] + list(map(int, sys.stdin))
visit = [None] + [0]*N
ans = []
for i in range(1, len(S)):
    if not visit[i]:
        ac = []
        if i == dfs(S, visit, i, ac):
            ans.extend(ac)
        else:
            for i in ac:
                visit[i] = 0

ans.sort()
print(len(ans))
print(*ans, sep='\n')
