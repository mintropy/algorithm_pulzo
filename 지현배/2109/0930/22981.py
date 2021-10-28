import sys
input = sys.stdin.readline
N, K = map(int, input().split())
arr = sorted(list(map(int, input().split())))
vmax = 0
for i in range(1, N):
    v1 = arr[0] * i
    v2 = arr[i] * (N - i)
    vmax = max(vmax, v1 + v2)
print(int(K / vmax + (1 if K % vmax else 0)))