import sys
input = sys.stdin.readline

_, W = map(int, input().split())
blocks = list(map(int, input().split()))

ans = 0
for i in range(1, W - 1):
    left = right = blocks[i]
    for j in range(0, i):
        if left < blocks[j]:
            left = blocks[j]
    for j in range(i + 1, W):
        if right < blocks[j]:
            right = blocks[j]
    low = min(left, right)
    if low > blocks[i]:
        ans += low - blocks[i]
print(ans)