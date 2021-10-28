import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
def find(n):
    if djs[n] == n:
        return n
    p = find(djs[n])
    djs[n] = p
    return p

N, M = map(int, input().split())
djs = [i for i in range(N + 1)]
ans = 0
for i in range(1, M + 1):
    s, e = map(lambda x: find(int(x)), input().split())
    if s != e:
        djs[s] = e
    else:
        ans = i
        break
print(ans)