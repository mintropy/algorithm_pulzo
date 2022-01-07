import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    x, y = map(int, input().split())
    dist = y - x
    sqrt_dist = int(dist ** 0.5)
    ans = 2 * sqrt_dist - 1
    if sqrt_dist != dist ** 0.5:
        if dist - sqrt_dist ** 2 > sqrt_dist:
            ans += 2
        else:
            ans += 1
    print(ans)