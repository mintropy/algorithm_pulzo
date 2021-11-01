import math
import sys

input = sys.stdin.readline

MIIS = lambda: map(int, input().split())
N, K = MIIS()
arr = list(MIIS())


def sol(arr):
    ave = sum(arr) / len(arr)
    disper = 0
    for a in arr:
        disper += (a - ave) * (a - ave)
    return disper / len(arr)


ans = 10 ** 12 * 500 + 1
for i in range(N - K + 1):
    for j in range(i + K, N + 1):
        ans = min(ans, sol(arr[i:j]))
print('{:.7f}'.format(math.sqrt(ans)))
