import sys

input = sys.stdin.readline

MIIS = lambda: map(int, input().split())

N, K = MIIS()
arr = list(MIIS())
arr.sort()

for _ in range(K):
    l, r, x = MIIS()
    for i in range(l-1, r):
        arr[i] = arr[i] + x


    arr.sort()
print(*arr)
