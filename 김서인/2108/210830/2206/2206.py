import sys, collections

input = sys.stdin.readline

# 4방향 상하좌우
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

N, M = map(int, input().split())
map = [[1] * (M + 2)] + list([1] + list(map(int, input().rstrip())) + [1] for _ in range(N)) + [
    [1] * (M + 2)]  # 인덱스 편하게 쓰려고 벽으로 패딩 만들어줌
visit = [[[0] * (M + 2) for _ in range(N + 2)] for _ in range(2)]  # 벽 부셨는지 여부, 방문 체크 - i, j

Q = collections.deque()
Q.append((1, 1, 0, 1))  # 출발점의 인덱스, 벽 부셨나(0 or 1), 거리

ans = []

while Q:
    i, j, canBreak, distance = Q.popleft()

    if i == N and j == M:  # 도착이면
        ans.append(distance)

    for k in range(4):
        ni = i + direction[k][0]
        nj = j + direction[k][1]

        if 0 < ni < N + 2 and 0 < nj < M + 2:  # 범위 이내이고
            if visit[1][ni][nj] == 0 and map[ni][nj] == 1 and canBreak == 0:  # 방문 안했고, 벽인데 갈 수 있다면 가보기
                visit[1][ni][nj] = 1  # 방문 체크
                Q.append((ni, nj, 1, distance + 1))

            if visit[canBreak][ni][nj] == 0 and map[ni][nj] == 0:  # 방문 안했고 길이면
                visit[canBreak][ni][nj] = 1  # 방문 체크
                Q.append((ni, nj, canBreak, distance + 1))  # 벽 안 부수고 가보기

if ans:
    print(min(ans))  # 벽 부수고, 안 부수고 둘 다 도달 가능하면 그 중 최소값을 답으로
else:
    print(-1)  # 못 도달하는 경우
