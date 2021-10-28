import sys
input = sys.stdin.readline
N, K = map(int, input().split())
ans = 'NO'
def calc(n):
    return n * (N - n) + N + 1

def BS(s, e):
    global ans
    if s >= e:
        if calc(s) == K:
            ans = 'YES'
        return
    m = (s + e) // 2
    res = calc(m)
    if res == K:
        ans = 'YES'
        return
    elif res > K:
        BS(s, m - 1)
    else:
        BS(m + 1, e)
BS(0, N // 2 + 1)
print(ans)