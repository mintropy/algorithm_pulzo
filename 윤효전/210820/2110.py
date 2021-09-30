import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline


def possible(mid):
    cnt = 1
    last = S[0]
    for n in S:
        if n - last >= mid:
            cnt += 1
            last = n
    return cnt >= C


N, C = map(int, input().split())
S = sorted([int(input()) for _ in range(N)])

l = 1
r = S[-1] - S[0]
ans = l

while l <= r:
    mid = (l+r)//2
    if possible(mid):
        ans = max(ans, mid)
        l = mid + 1
    else:
        r = mid - 1

print(ans)
