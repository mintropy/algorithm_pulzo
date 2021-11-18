import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
ans = 0


# 기울기
def slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)


for i in range(N):
    # 왼쪽
    left = 0

    if i - 1 >= 0:  # 더 갈 곳이 있으면
        before_slope = slope(i, arr[i], i - 1, arr[i - 1])
        left += 1

        # i-1~ 0까지 점점 기울기가 작아져야 함
        for j in range(i - 2, -1, -1):
            tmp = slope(i, arr[i], j, arr[j])
            if tmp < before_slope:
                left += 1
                before_slope = tmp

    # 오른쪽
    right = 0
    if i + 1 <= N - 1:
        before_slope = slope(i, arr[i], i + 1, arr[i + 1])
        right += 1

        # i+1~ N-1까지 점점 기울기가 커져야 함
        for j in range(i + 2, N):
            tmp = slope(i, arr[i], j, arr[j])
            if tmp > before_slope:
                right += 1
                before_slope = tmp

    ans = max(ans, left + right)
print(ans)
