import sys

input = sys.stdin.readline

MIIS = lambda: map(int, input().split())

N = int(input())

bus_route = []

for _ in range(N):
    S, E, C = MIIS()
    bus_route.append((S, E, C))

# 정렬
bus_route.sort()

result_route = []

a_route = bus_route[0]  # 처음 노선
for i in range(1, N):
    # 두 노선을 보면서
    b_route = bus_route[i]

    # 겹치면 합쳐서 새로운 노선으로 만들기
    if a_route[1] >= b_route[0]:
        a_route = (a_route[0], max(a_route[1], b_route[1]), min(a_route[2], b_route[2]))

    else:  # 안 겹치면 그때까지 합친 노선을 새롭게 result_route에 추가하고, 새로운 노선 만들기
        result_route.append(a_route)
        a_route = bus_route[i]

# 반영 안한 노선 있으면 반영
if a_route not in result_route:
    result_route.append(a_route)

print(len(result_route))
for route in result_route:
    print(*route)
