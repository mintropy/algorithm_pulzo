import sys

input = sys.stdin.readline

N, M = map(int, input().split())
times = list(int(input()) for _ in range(N))

left = 1
right = min(times) * M
ans = right


def calculate_screening_cnt(time: int) -> int:
    """심사관들이 time초 동안 몇 명을 심사할 수 있는지 구하는 함수"""
    cnt = 0
    for i in times:
        cnt += (time // i)
    return cnt


while left <= right:
    mid = (right + left) // 2

    can_screening_cnt = calculate_screening_cnt(mid)
    if can_screening_cnt < M:
        left = mid + 1

    else:
        ans = min(ans, mid)
        right = mid - 1

print(ans)
