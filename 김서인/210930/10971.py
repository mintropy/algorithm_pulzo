import sys

input = sys.stdin.readline

N = int(input())

cost_matrix = list(list(map(int, input().split())) for _ in range(N))


def dfs(curr_city, total_cost):
    global smallest_cost

    if total_cost > smallest_cost: # 이미 최솟값 아니라면
        return

    if curr_city == k and visited[k] == 2:  # 다시 돌아왔으면
        for v in visited:
            if v == 0:  # 방문 안 한 곳 있으면
                return
        smallest_cost = min(smallest_cost, total_cost)
        return

    for i in range(N):
        next_city_cost = cost_matrix[curr_city][i]
        if next_city_cost != 0 and i == k:  # 출발지로 가는 경우
            visited[i] += 1
            dfs(i, total_cost + next_city_cost)
            visited[i] -= 1

        if next_city_cost != 0 and visited[i] == 0:  # 갈 수 있고, 방문하지 않은 곳이라면
            visited[i] += 1
            dfs(i, total_cost + next_city_cost)
            visited[i] -= 1


smallest_cost = 1000000 * 10
for k in range(N):
    visited = [0] * N  # 도시 방문 체크
    # 모든 도시에서 시작해보기
    visited[k] = 1
    dfs(k, 0)  # 출발 도시, 비용

print(smallest_cost)
