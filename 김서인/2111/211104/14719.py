import sys

input = sys.stdin.readline
MIIS = lambda: map(int, input().split())
H, W = MIIS()
arr = list(MIIS())

ans = 0


def is_poll(depth, width):
    if width == 0 or width == W - 1:
        return False

    flag1 = False
    flag2 = False
    # 좌
    for i in range(width):
        if arr[i] > depth:
            flag1 = True
            break
    # 우
    for i in range(width + 1, W):
        if arr[i] > depth:
            flag2 = True
            break

    if flag1 == True and flag2 == True:
        return True
    else:
        return False


# 맨 아래부터
for depth in range(min(arr), max(arr)):
    for j in range(W):
        # 빈 칸
        if depth >= arr[j]:
            # 좌우에 자기보다 큰 수 있으면 더하기
            if is_poll(depth, j):
                ans += 1

print(ans)
