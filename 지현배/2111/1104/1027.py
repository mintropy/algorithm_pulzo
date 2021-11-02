import sys
input = sys.stdin.readline

N = int(input())
buildings = tuple(map(int, input().split()))
ans = 0

for i in range(N):
    cnt = 0
    # left
    if i > 0:
        cnt += 1
        gradient = buildings[i] - buildings[i - 1]
        for j in range(i - 2, -1, -1):
            next_gradient = (buildings[i] - buildings[j]) / (i - j)
            if gradient > next_gradient:
                cnt += 1
                gradient = next_gradient
    
    # right
    if i < N - 1:
        cnt += 1
        gradient = buildings[i] - buildings[i + 1]
        for j in range(i + 2, N):
            next_gradient = (buildings[i] - buildings[j]) / (j - i)
            if gradient > next_gradient:
                cnt += 1
                gradient = next_gradient
    ans = max(ans, cnt)
print(ans)