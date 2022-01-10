import heapq
import sys

input = sys.stdin.readline

C, N = map(int, input().strip().split())

chickens = sorted(list(int(input().strip()) for _ in range(C)))

cows = sorted(list(tuple(map(int, input().strip().split())) for _ in range(N)), key=lambda x: (x[0], x[1]))

watch_zones = set(chickens)

cow_check_left = list(map(lambda cow: cow[0], cows))
watch_zones = watch_zones.union(set(cow_check_left))

cow_check_right = list(map(lambda cow: cow[1] + 1, cows))
watch_zones = watch_zones.union(set(cow_check_right))

watch_zones = sorted(list(watch_zones))  # 체크할 지점들

ans = 0
q = list()  # 도움 받을 소가 들어 있음.
for time in watch_zones:
    # 소가 들어갈 수 있으면(시작점)
    while cows:
        if cows[0][0] == time:
            heapq.heappush(q, cows[0][1])  # 도착점 넣기
            del cows[0]
        else:
            break

    # 소가 시간 내에 도움 못 받으면
    while q:
        if q[0] < time:
            heapq.heappop(q)  # 소 퇴출
        else:
            break

    # 닭의 도움 받을 소가 있으면
    while chickens:
        if chickens[0] == time:
            chickens.pop(0)
            if q:
                heapq.heappop(q)
                ans += 1
        else:
            break

print(ans)
