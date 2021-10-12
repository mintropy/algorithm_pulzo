import sys
input = sys.stdin.readline
N, M = map(int, input().split())
ans = 0
H = []
if N: H = list(map(int, input().split()))
Hcnt = len(H)
Hsum = sum(H)
no = M - (Hcnt + Hsum)
if no > 0:
    cnt = 1
    for _ in range(no // (Hcnt + 1)):
        ans += (Hcnt + 1) * (cnt ** 2)
        cnt += 1
    ans += (no % (Hcnt + 1)) * (cnt ** 2)
print(ans)