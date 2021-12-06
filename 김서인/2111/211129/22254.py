import heapq
import sys

input = sys.stdin.readline

MIISS = lambda: map(int, input().strip().split())

N, X = MIISS()
make_times = list(MIISS())

ans = 100001

left = 1
right = N

while left <= right:
    mid = (left + right) // 2  # 공정 라인의 개수
    hq = [0] * (mid)  # 어떤 공정 라인 쓸 건지(사용 시간을 담음)

    # 공정 라인 mid개로 선물 N개 주문 제작 시 걸리는 시간 구하기
    for time in make_times:
        tmp = heapq.heappop(hq)
        heapq.heappush(hq, tmp + time)

    need_time = max(hq)

    # 선물 제작 시간이 X 시간 이하이면
    if need_time <= X:
        right = mid - 1
        ans = min(ans, mid)
    # 선물 제작 시간이 X 시간 초과이면
    else:
        left = mid + 1

print(ans)
