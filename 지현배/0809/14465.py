import sys
input = sys.stdin.readline

def sol():
    N, K, B = map(int, input().split())
    light = [1 for _ in range(N + 1)]
    for _ in range(B):
        light[int(input())] = 0
    ptr = 2
    minCnt = N
    cnt = light[1:K + 1].count(0)
    while ptr + K - 1 < N + 1:
        if light[ptr + K - 1] == 0:
            cnt += 1
        if light[ptr - 1] == 0:
            cnt -= 1
        minCnt = min(minCnt, cnt)
        ptr += 1
    return minCnt
print(sol())
